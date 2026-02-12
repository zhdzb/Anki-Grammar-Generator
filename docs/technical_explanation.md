# 技术原理说明：从 CSV 到 APKG 的自动化构建

本文档解释了我们如何通过 Python 脚本将原始 CSV 数据转换为功能完备的 Anki 牌组包 (.apkg)。

## 1. 核心问题

直接导入 CSV 到 Anki 时存在以下局限性：
*   **手动配置繁琐**：用户必须手动创建“笔记类型 (Note Type)”，定义 9 个字段，并手动将每一列映射到字段。
*   **样式丢失**：CSV 纯文本无法携带 CSS 样式，用户必须手动去编辑卡片模板代码。
*   **字段丢失风险**：如果用户选择的 Note Type 只有“正面”和“背面”两个字段，CSV 中的后 7 列数据（例句、接续、辨析等）会被直接丢弃。

## 2. 解决方案：程序化生成 (Programmatic Generation)

我们使用 Python 的 `genanki` 库，模拟了 Anki 内部的数据结构，将“数据”和“结构”打包在一起。

### A. 定义数据模型 (The Model)

在脚本中，我们定义了一个名为 `N5_Grammar_Model` 的对象。这相当于在 Anki 中新建了一个“高级笔记类型”。

```python
# 对应 Anki 中的 "Tools -> Manage Note Types"
N5_MODEL = genanki.Model(
    1607392319,  # 唯一的 Model ID
    'N5 Grammar Model',
    fields=[
        # 显式定义 9 个字段，与 CSV 列一一对应
        {'name': 'Grammar'},
        {'name': 'Meaning'},
        {'name': 'Connection'},
        # ... (其他字段)
    ],
    templates=[
        {
            'name': 'Card 1',
            # 嵌入 HTML 模板
            'qfmt': FRONT_TEMPLATE,
            'afmt': BACK_TEMPLATE,
        },
    ],
    css=CSS  # 嵌入 CSS 样式
)
```

**原理**：
1.  **字段绑定**：我们告诉 Anki，这个牌组里的卡片天生就有 `Simple_Example_JP` 等字段。
2.  **模板注入**：我们将之前设计的 HTML/CSS 直接注入到 Model 中。当您打开卡片时，Anki 会自动渲染这些代码。

### B. 数据注入 (Data Injection)

脚本读取 `japanese_grammar.csv`，逐行处理：

```python
for row in reader:
    note = genanki.Note(
        model=N5_MODEL,
        fields=row[0:9]  # 将 CSV 的一行数据填入 Model 的 9 个空槽
    )
    N5_DECK.add_note(note)
```

**原理**：
每一行 CSV 数据被转换成一个 `Note` 对象。因为 `Note` 是基于 `N5_MODEL` 创建的，它自动继承了模板和样式。

### C. 打包 (Packaging)

最后，`genanki.Package(N5_DECK).write_to_file(...)` 将所有内容（数据库结构、模板、数据）压缩成一个 SQLite 数据库格式的 `.apkg` 文件。

## 3. apkg vs csv

当您导入 `.apkg` 文件时：
1.  Anki 读取文件头，发现里面包含一个新的 **Note Type (N5 Grammar Model)**。
2.  Anki 自动将这个 Note Type 安装到您的系统中（包含所有字段定义和 CSS）。
3.  Anki 将数据填充进去。

相比之下，导入 CSV 只是“灌入数据”，它假设容器（Note Type）已经存在且形状匹配。使用 `.apkg` 则是“连容器带数据”一起交付，因此做到了**零配置、零丢失**。
