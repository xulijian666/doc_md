"""
需规文档抽取 · 本体映射 - Flask Web 应用
选择文件/文件夹 → 转换 → MD 和 _files 生成在源文件所在目录
"""
import os
import sys
import shutil
import time
import threading
import uuid
import zipfile
import io
from pathlib import Path
from flask import Flask, request, jsonify, render_template, send_file

SCRIPTS_DIR = Path(__file__).parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

try:
    from docx2md import docx_to_md, xlsx_to_md, pdf_to_md, doc_to_docx
except ImportError as e:
    print(f"[ERROR] 导入 docx2md 失败: {e}")
    print("[ERROR] 请运行: pip install -r requirements.txt")
    sys.exit(1)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024

SUPPORTED_EXTS = {'.docx', '.doc', '.xlsx', '.xls', '.pdf'}
TEMP_DIR = Path(__file__).parent / "_temp"
TEMP_DIR.mkdir(exist_ok=True)

# 临时文件过期清理：1 小时
TEMP_EXPIRE_SECS = 1800


def _cleanup_expired():
    """删除 _temp 中超过 1 小时未修改的会话目录"""
    while True:
        try:
            now = time.time()
            for d in TEMP_DIR.iterdir():
                if d.is_dir():
                    mtime = d.stat().st_mtime
                    if now - mtime > TEMP_EXPIRE_SECS:
                        shutil.rmtree(d, ignore_errors=True)
                        print(f"[cleanup] 已清理过期会话: {d.name}")
        except Exception:
            pass
        time.sleep(600)  # 每 10 分钟检查一次


# 启动后台清理线程（daemon，随主进程退出）
_thread = threading.Thread(target=_cleanup_expired, daemon=True)
_thread.start()


@app.errorhandler(Exception)
def handle_exception(e):
    from flask import request as req
    if req.path.startswith('/api/'):
        return jsonify({'error': str(e)}), 500
    return e


def get_file_type(suffix):
    mapping = {
        '.docx': 'Word', '.doc': 'Word (旧)',
        '.xlsx': 'Excel', '.xls': 'Excel (旧)',
        '.pdf': 'PDF'
    }
    return mapping.get(suffix, '未知')


def convert_single(input_path: Path, output_dir: Path) -> dict:
    suffix = input_path.suffix.lower()
    output_dir.mkdir(parents=True, exist_ok=True)

    if suffix in ('.xlsx', '.xls'):
        md_path = xlsx_to_md(str(input_path), str(output_dir))
    elif suffix == '.docx':
        md_path = docx_to_md(str(input_path), str(output_dir))
    elif suffix == '.doc':
        tmp_docx = doc_to_docx(str(input_path))
        try:
            md_path = docx_to_md(tmp_docx, str(output_dir))
        finally:
            try:
                os.remove(tmp_docx)
                os.rmdir(str(Path(tmp_docx).parent))
            except:
                pass
    elif suffix == '.pdf':
        md_path = pdf_to_md(str(input_path), str(output_dir))
    else:
        return {'name': input_path.name, 'status': 'error', 'message': f'不支持的格式: {suffix}'}

    md_content = Path(md_path).read_text(encoding='utf-8')
    md_stem = Path(md_path).stem
    assets_dir = output_dir / f"{md_stem}_files"
    images_count = 0
    attachments_count = 0
    if assets_dir.exists():
        img_dir = assets_dir / "images"
        att_dir = assets_dir / "attachments"
        if img_dir.exists():
            images_count = len(list(img_dir.iterdir()))
        if att_dir.exists():
            attachments_count = len(list(att_dir.iterdir()))

    return {
        'name': input_path.name,
        'status': 'success',
        'md_name': Path(md_path).name,
        'md_path': str(md_path),
        'content': md_content,
        'images': images_count,
        'attachments': attachments_count
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_files():
    """接收上传文件，暂存到临时目录，返回文件列表"""
    files = request.files.getlist('files')
    if not files:
        return jsonify({'error': '未选择文件'}), 400

    TEMP_DIR.mkdir(exist_ok=True)
    session_id = str(uuid.uuid4())[:8]
    session_dir = TEMP_DIR / session_id
    session_dir.mkdir(exist_ok=True)

    errors = []
    file_list = []
    for f in files:
        if not f.filename:
            continue
        filename = f.filename.replace('\\', '/')
        suffix = Path(filename).suffix.lower()
        if suffix not in SUPPORTED_EXTS:
            errors.append(f"{Path(filename).name} (不支持格式: {suffix})")
            continue

        save_path = session_dir / Path(filename).name
        f.save(str(save_path))

        file_list.append({
            'name': Path(filename).name,
            'relative_path': Path(filename).name,
            'temp_path': str(save_path),
            'size': save_path.stat().st_size,
            'type': get_file_type(suffix),
            'suffix': suffix
        })

    if not file_list and errors:
        shutil.rmtree(session_dir, ignore_errors=True)
        return jsonify({'error': '所有文件均不支持。\n' + '\n'.join(errors)}), 400

    result = {'session_id': session_id, 'files': file_list, 'count': len(file_list)}
    if errors:
        result['warnings'] = errors
    return jsonify(result)


@app.route('/api/convert', methods=['POST'])
def convert_files():
    """转换文件，输出到源文件所在目录（原位生成）"""
    data = request.json
    session_id = data.get('session_id')
    selected_files = data.get('files', [])

    if not session_id or not selected_files:
        return jsonify({'error': '参数不完整'}), 400

    session_dir = TEMP_DIR / session_id
    if not session_dir.exists():
        return jsonify({'error': '会话已过期，请重新上传'}), 400

    results = []
    for file_info in selected_files:
        temp_path = Path(file_info['temp_path'])
        if not temp_path.exists():
            results.append({'name': file_info['name'], 'status': 'error', 'message': '文件不存在'})
            continue

        try:
            # 输出到源文件所在目录
            out = temp_path.parent
            result = convert_single(temp_path, out)
            results.append(result)
        except Exception as e:
            results.append({'name': file_info['name'], 'status': 'error', 'message': str(e)})

    return jsonify({'results': results})


@app.route('/api/download/<session_id>/<path:filename>')
def download_file(session_id, filename):
    """下载生成的 md 文件"""
    file_path = TEMP_DIR / session_id / filename
    if file_path.exists():
        return send_file(str(file_path), as_attachment=True)
    return jsonify({'error': '文件不存在'}), 404


@app.route('/api/download-zip/<session_id>/<md_name>')
def download_zip(session_id, md_name):
    """打包下载单个 MD 文件及其 _files 资源文件夹"""
    session_dir = TEMP_DIR / session_id
    md_path = session_dir / md_name
    if not md_path.exists():
        return jsonify({'error': '文件不存在'}), 404

    stem = Path(md_name).stem
    files_dir = session_dir / f"{stem}_files"

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(md_path, md_name)
        if files_dir.exists():
            for f in files_dir.rglob('*'):
                if f.is_file():
                    zf.write(f, f.relative_to(session_dir))
    buf.seek(0)

    return send_file(buf, as_attachment=True, download_name=f"{stem}.zip", mimetype='application/zip')


@app.route('/api/download-all/<session_id>')
def download_all(session_id):
    """打包下载会话中所有生成的 MD 和 _files（不含原始文件）"""
    session_dir = TEMP_DIR / session_id
    if not session_dir.exists():
        return jsonify({'error': '会话不存在'}), 404

    # 收集所有原始文件名（不含扩展名），用于判断哪些是生成的
    original_stems = set()
    for p in session_dir.iterdir():
        if p.suffix in SUPPORTED_EXTS:
            original_stems.add(p.stem)

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        for p in session_dir.iterdir():
            # 只打包由转换生成的 .md 文件
            if p.suffix == '.md' and p.stem in original_stems:
                zf.write(p, p.name)
            # 打包 _files 资源文件夹
            elif p.is_dir() and p.name.endswith('_files'):
                for f in p.rglob('*'):
                    if f.is_file():
                        zf.write(f, f.relative_to(session_dir))
    buf.seek(0)

    return send_file(buf, as_attachment=True, download_name='转换结果.zip', mimetype='application/zip')


if __name__ == '__main__':
    print("=" * 50)
    print("  需规文档抽取 · 本体映射")
    print("  访问 http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
