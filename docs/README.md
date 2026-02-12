# 日语 N5 文法 Anki 卡片规范 (进阶版)

本文档更新了 Anki 卡片设计，以满足 **“多维挑战 + 易混淆辨析”** 的学习需求。

## 1. 设计理念

*   **正面 (Challenge)**：一次性提供三个线索，全方位激活记忆。
    1.  **中文含义**：让你联想文法形式。
    2.  **简单例句 (日)**：让你在基础语境中确认文法。
    3.  **挑战难句 (日)**：让你在复杂语境中尝试理解/翻译。
*   **背面 (Answer)**：提供所有线索的对应答案，并重点讲解**易混淆文法**。

## 2. 数据格式

- **文件**: `japanese_grammar.csv`
- **字段数**: 9 个字段

| 序号 | 字段名 | 说明 | 示例 |
| :--- | :--- | :--- | :--- |
| 1 | **Grammar** | 文法条目 | `～に` |
| 2 | **Meaning** | 中文含义 | `在... (存在的地点)` |
| 3 | **Connection** | 接续形式 | `場所 ＋ に` |
| 4 | **Simple_Example_JP** | 简单例句 (日) | `庭に犬がいます。` |
| 5 | **Simple_Example_CN** | 简单例句 (中) | `院子里有狗。` |
| 6 | **Hard_Example_JP** | **挑战难句 (日)** | `昔、この静かな...` |
| 7 | **Hard_Example_CN** | 难句翻译 (中) | `很久以前...` |
| 8 | **Similar_Grammar** | **易混淆文法** | `～で (動作)` |
| 9 | **Difference** | **辨析/用法对比** | `に表静态，で表动态...` |

## 3. 卡片模板 (Card Template)

### 正面模板 (Front Template)

```html
<div class="card-content">
    <!-- 挑战1: 含义 -->
    <div class="section-title">含义</div>
    <div class="meaning">{{Meaning}}</div>
    
    <hr class="separator">

    <!-- 挑战2: 文法/简单句 -->
    <div class="section-title">文法 / 简单句</div>
    <div class="grammar-display">{{Grammar}}</div>
    <div class="example-jp simple">{{Simple_Example_JP}}</div>
    
    <hr class="separator">

    <!-- 挑战3: 难句挑战 -->
    <div class="section-title">🔥 难句挑战</div>
    <div class="example-jp hard">{{Hard_Example_JP}}</div>

    <div class="instruction">
        🤔 思考：
        1. 这个文法怎么用？
        2. 难句是什么意思？
        3. 它和 {{Similar_Grammar}} 有什么区别？
    </div>
</div>
```

### 背面模板 (Back Template)

```html
<div class="card-content">
    <!-- 顶部重复正面内容，但可以淡化 -->
    <div class="front-review">
        <div class="grammar-display">{{Grammar}}</div>
        <div class="meaning">{{Meaning}}</div>
    </div>
    
    <hr>
    
    <!-- 答案区域 -->
    <div class="answer-box">
        <div class="label">简单句翻译</div>
        <div class="example-cn">{{Simple_Example_CN}}</div>
        
        <div class="label" style="margin-top: 15px;">🔥 难句翻译</div>
        <div class="example-cn">{{Hard_Example_CN}}</div>
    </div>
    
    <!-- 辨析区域 (如果有易混淆点才显示) -->
    {{#Difference}}
    <div class="confusion-box">
        <div class="confusion-title">⚠️ 易混淆辨析：{{Similar_Grammar}}</div>
        <div class="confusion-content">{{Difference}}</div>
    </div>
    {{/Difference}}
    
    <div class="connection-info">接续：{{Connection}}</div>
</div>
```

### 样式表 (Styling)

```css
.card {
    font-family: "Yu Mincho", "Hiragino Mincho Pro", "Microsoft YaHei", serif;
    font-size: 18px;
    text-align: center;
    color: #333;
    background-color: #f9f9f9;
}

.card-content {
    max-width: 600px;
    margin: 0 auto;
    padding: 10px;
}

.section-title {
    font-size: 12px;
    color: #999;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 10px;
}

.grammar-display {
    font-size: 28px;
    font-weight: bold;
    color: #2c3e50;
    margin: 5px 0;
}

.meaning {
    font-size: 22px;
    color: #e74c3c;
    font-weight: bold;
}

.example-jp {
    font-size: 20px;
    margin: 10px 0;
    line-height: 1.6;
}

.example-jp.hard {
    background: #fff3e0;
    padding: 10px;
    border-radius: 6px;
    border: 1px dashed #f39c12;
}

.separator {
    border: 0;
    border-top: 1px solid #eee;
    margin: 15px 0;
}

.instruction {
    font-size: 14px;
    color: #aaa;
    margin-top: 30px;
    font-style: italic;
}

/* 背面样式 */
.front-review {
    opacity: 0.7;
    font-size: 0.8em;
}

.answer-box {
    text-align: left;
    background: white;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.label {
    font-size: 12px;
    color: #7f8c8d;
    font-weight: bold;
}

.example-cn {
    font-size: 16px;
    color: #555;
    margin-top: 5px;
}

.confusion-box {
    margin-top: 20px;
    text-align: left;
    background: #ffebee;
    border-left: 4px solid #e57373;
    padding: 10px 15px;
    border-radius: 4px;
}

.confusion-title {
    font-weight: bold;
    color: #c0392b;
    margin-bottom: 5px;
}

.confusion-content {
    font-size: 15px;
    color: #333;
}

.connection-info {
    margin-top: 20px;
    font-size: 14px;
    color: #95a5a6;
    background: #ecf0f1;
    display: inline-block;
    padding: 4px 10px;
    border-radius: 12px;
}
```
