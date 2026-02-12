# JLPT Anki Deck Generator

这是一个自动生成 JLPT (N5-N1) 文法 Anki 牌组的工具。旨在帮助学习者高效记忆和复习日语文法。

## 项目结构 (Project Structure)

```
anki/
├── data/                   # 数据源
│   └── n5_grammar.csv      # N5 文法数据 (支持添加 n4_grammar.csv, n3_grammar.csv 等)
├── docs/                   # 文档
│   ├── n5_rules.md         # N5 数据生成规范 & 大纲
│   └── technical_explanation.md # 技术原理说明
├── output/                 # 输出产物
│   └── N5_Grammar.apkg     # 生成的 Anki 牌组文件
├── src/                    # 源代码
│   ├── templates/          # HTML/CSS 模板 (通用)
│   │   ├── front.html
│   │   ├── back.html
│   │   └── style.css
│   └── builder.py          # 自动化构建脚本
└── README.md               # 项目说明
```

## 如何使用 (Usage)

1.  **准备数据**:
    在 `data/` 目录下创建或编辑文法数据文件。文件命名必须遵循 `n{级别}_grammar.csv` 的格式，例如：
    *   `n5_grammar.csv`
    *   `n4_grammar.csv`
    *   `n1_grammar.csv`

2.  **修改样式 (可选)**:
    所有级别的牌组共用一套模板。如果需要调整卡片外观，请编辑 `src/templates/style.css`。

3.  **生成牌组**:
    在终端中运行以下命令：
    ```bash
    python src/builder.py
    ```
    脚本会自动扫描 `data/` 目录下的所有符合命名规则的 CSV 文件，并在 `output/` 目录生成对应的 `.apkg` 文件（如 `N5_Grammar.apkg`, `N4_Grammar.apkg`）。

4.  **导入 Anki**:
    双击 `output/` 目录下的 `.apkg` 文件即可导入到 Anki 桌面版或移动版。

## 依赖 (Dependencies)

*   Python 3.x
*   genanki (`pip install genanki`)
