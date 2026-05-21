# B2 需规文档知识管理 —— Demo准备方案

## 一、会前准备清单

### 第1步：搭环境（约30分钟）

| 事项 | 动作 | 说明 |
|------|------|------|
| Python环境 | 确认Python 3.9+已安装 | `python --version` |
| 安装依赖 | `pip install python-docx flashtext` | python-docx做转换，flashtext做打标 |
| 安装Obsidian | 下载安装Obsidian客户端 | 免费，官网直接下 |
| 建Obsidian库 | 用Obsidian打开 `D:\CODE\doc_md\obsidian_doc` 目录 | 作为知识库根目录 |

### 第2步：准备输入素材

**素材A：一份Word需求文档**

准备一份2-3页的需求文档，内容包括：
- 需求背景
- 业务流程描述（涉及保险术语）
- 功能点列表
- 验收标准

> 这份文档就是演示时的"输入"，模拟业务人员写的原始Word。

**素材B：本体术语清单**

一个JSON文件，mock十几个保险术语即可。后续角色一交付真正的本体后替换这个文件。

文件名：`ontology_terms.json`

```json
[
  "犹豫期", "退保", "现金价值", "宽限期",
  "核保", "理赔", "受益人", "保单",
  "保费", "保险责任", "如实告知", "复效"
]
```

### 第3步：写两个脚本

**脚本1：`convert.py`** — DOCX转Markdown

- 输入：Word文件路径
- 输出：Markdown文件
- 功能：用python-docx提取标题层级、段落、表格、加粗，输出干净MD
- 工具：python-docx（https://github.com/python-openxml/python-docx）

**脚本2：`tag.py`** — 自动打标

- 输入：Markdown文件 + 术语清单JSON
- 输出：术语被替换为 `[[]]` 的新Markdown
- 功能：用Flashtext扫描，遇到术语自动加双链

### 第4步：跑通全流程（约1小时）

按这个顺序跑一遍，确保每步都能出结果：

```
1. 把Word文档放到 input/ 目录
2. 运行 python convert.py input/需求文档.docx -o output/需求文档.md
3. 检查 output/需求文档.md 内容是否正确
4. 运行 python tag.py output/需求文档.md --dict ontology_terms.json -o tagged/需求文档.md
5. 检查 tagged/需求文档.md 中的术语是否被加上了 [[]]
6. 把 tagged/ 目录的文件复制到 Obsidian 库中
7. 打开Obsidian，检查图谱视图是否正确显示链接
```

### 第5步：准备对比材料

| 材料 | 用途 |
|------|------|
| 原始Word文档截图 | 开场展示"这是业务人员写的原始文档" |
| 转换后的MD文件 | 展示"格式保留完整" |
| 打标前的MD（一份副本） | diff对比用 |
| 打标后的MD | 展示"术语自动加上双链" |
| Obsidian图谱截图 | 展示最终效果 |

> 提前截图存好，万一演示时环境出问题，可以用截图兜底。

---

## 二、会中演示流程（建议10分钟）

### 开场（1分钟）

> "我负责的是B2——需规文档知识管理。核心问题是：业务人员写的需求文档是Word格式的，怎么让大模型能读懂、能关联到本体？我的方案分两步：先转成Markdown，再自动打标挂载到本体。"

### 第一部分：需求文档转MD（4分钟）

**动作1**：展示原始Word文档

> "这是一份真实的网销退保功能需求文档，业务人员用Word写的，里面有标题、表格、加粗等格式。"

**动作2**：运行转换脚本

```bash
python convert.py input/网销退保需求.docx -o output/网销退保需求.md
```

> "一条命令，几秒钟，Word就转成了Markdown。"

**动作3**：打开生成的MD，展示效果

> "标题层级、表格、加粗全部保留。关键是：现在它是纯文本了，机器可以直接读取和处理。"

### 第二部分：MD文档管理（5分钟）

**动作4**：展示打标前的MD

> "转换后的Markdown里，保险术语就是普通文本。"

**动作5**：运行打标脚本

```bash
python tag.py output/网销退保需求.md --dict ontology_terms.json -o tagged/网销退保需求.md
```

**动作6**：diff对比打标前后

> "可以看到，'犹豫期'变成了'[[犹豫期]]'，'退保'变成了'[[退保]]'，系统自动识别了文档中的保险术语并加上双链。"

**动作7**：打开Obsidian，展示图谱视图

> "在Obsidian中，这篇需求文档和我们之前建的知识文档形成了关联网络。点击'退保'节点，可以看到所有涉及退保的文档。"

**动作8**：点击某个节点，展示反向链接

> "这就是反向链接——不需要人工维护，只要文档里提到了这个术语，就自动关联。"

### 总结（1分钟）

> "整个流程是：业务人员写Word → 系统自动转Markdown → 自动识别术语打标 → 知识图谱自动形成。后续大模型做需求分析时，就可以沿着这些双链精准检索到关联的业务知识。"

---

## 三、文件目录结构

```
D:\CODE\doc_md\
├── demo/
│   ├── convert.py              ← 转换脚本（python-docx）
│   ├── tag.py                  ← 打标脚本（flashtext）
│   ├── ontology_terms.json     ← 本体术语清单（mock）
│   ├── input/                  ← 原始Word文档
│   │   └── 网销退保需求.docx
│   ├── output/                 ← 转换后的MD
│   │   └── 网销退保需求.md
│   └── tagged/                 ← 打标后的MD
│       └── 网销退保需求.md
├── obsidian_doc/
│   └── 本体_资料库/            ← 知识文档（已有6篇）
│       ├── 产品条款.md
│       ├── 网销渠道投保操作手册.md
│       ├── 退保与退费处理办法.md
│       ├── 理赔报案与调查手册.md
│       ├── 续期保费催缴与宽限期处理办法.md
│       ├── 保全业务管理办法.md
│       └── 网销退保需求.md     ← 演示时复制进来
└── skills/
```

---

## 四、会前Checklist

- [ ] Python环境就绪，python-docx和flashtext安装成功
- [ ] Obsidian安装完成，能打开 `obsidian_doc` 目录
- [ ] `ontology_terms.json` 准备好（12个术语）
- [ ] 一份Word需求文档准备好（2-3页）
- [ ] `convert.py` 写好并跑通
- [ ] `tag.py` 写好并跑通
- [ ] 全流程跑通一遍，确认Obsidian图谱正常显示
- [ ] 关键步骤截图备份（防现场翻车）
- [ ] 演示话术过一遍
