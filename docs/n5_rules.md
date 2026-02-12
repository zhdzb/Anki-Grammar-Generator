# Anki 卡片生成约束规范 (Generation Constraints)

为了保持 N5 文法卡片的一致性和高质量，所有新卡片的生成必须遵循以下约束。

## 1. 核心约束 (Core Constraints)

*   **目标级别**: JLPT N5 (参考《大家的日语》初级1 L1-L25)
*   **文件格式**: CSV (UTF-8)
*   **字段结构**:
    1.  `Grammar`: 文法条目
    2.  `Meaning`: 中文含义
    3.  `Connection`: 接续形式
    4.  `Simple_Example_JP`: 简单例句 (必须含 `<ruby>`)
    5.  `Simple_Example_CN`: 简单例句翻译
    6.  `Hard_Example_JP`: 挑战难句 (必须含 `<ruby>`)
    7.  `Hard_Example_CN`: 挑战难句翻译
    8.  `Similar_Grammar`: 易混淆文法 (可选，无则留空)
    9.  `Difference`: 辨析说明 (可选，无则留空)

## 2. 内容质量标准 (Quality Standards)

### A. 振假名 (Furigana)
*   **规则**: 所有汉字必须标注平假名。
*   **格式**: 使用 HTML Ruby 标签。
    *   正确: `<ruby>学生<rt>がくせい</rt></ruby>`

### B. 例句设计 (Sentence Design)
*   **简单句**: 结构简单，长度控制在 10-20 字以内。
*   **难句**: 包含从句、修饰语或更复杂的语境，长度 20-40 字。

## 3. N5 完整文法大纲 (Syllabus)

### 第一部分：名词与基础助词 (L1-L7)
- [x] ～は～です (L1)
- [x] ～か (Question) (L1)
- [x] ～の (Possession) (L1)
- [x] ～も (Also) (L1)
- [x] ～はありません / ～じゃありません (Negation) (L1)
- [x] ～これ/それ/あれ (Demonstratives) (L2)
- [x] ～ここ/そこ/あそこ (Place) (L3)
- [x] ～ます/ません/ました (Verb Tense) (L4)
- [x] ～へ (Direction) (L5)
- [x] ～で (Transport/Tool) (L5/L7)
- [x] ～と (With person) (L5)
- [x] ～を (Object) (L6)
- [x] ～で (Place of action) (L6)
- [x] ～ませんか (Invitation) (L6)
- [x] ～ましょう (Let's) (L6)
- [x] ～あげます/もらいます (Give/Receive) (L7)

### 第二部分：形容词与存在 (L8-L12)
- [x] い形容詞 (Present/Past/Neg) (L8/L12)
- [x] な形容詞 (Present/Past/Neg) (L8/L12)
- [x] ～は～が (Like/Dislike/Skill) (L9)
- [x] ～わかります/あります (Understand/Possess) (L9)
- [x] ～に～がいます/あります (Existence) (L10)
- [x] ～助数詞 (Counters) (L11)
- [x] ～より (Comparison) (L12)
- [x] ～のほうが (Comparison) (L12)
- [x] ～で～がいちばん (Superlative) (L12)

### 第三部分：动词活用初级 (L13-L16)
- [x] ～たいです (Desire) (L13)
- [x] ～に行きます (Purpose) (L13)
- [x] ～てください (Request) (L14)
- [x] ～ましょうか (Offer help) (L14)
- [x] ～ています (Progressive/State) (L15)
- [x] ～てもいいです (Permission) (L15)
- [x] ～てはいけません (Prohibition) (L15)
- [x] ～て、～て (Sequence) (L16)

### 第四部分：动词活用进阶 (L17-L20)
- [x] ～ないでください (Negative Request) (L17)
- [x] ～なければなりません (Must) (L17)
- [x] ～なくてもいいです (No need) (L17)
- [x] ～ことができます (Potential) (L18)
- [x] ～趣味は～ことです (Hobby) (L18)
- [x] ～まえに (Before) (L18)
- [x] ～たことがあります (Experience) (L19)
- [x] ～たり～たり (Listing) (L19)
- [x] ～なります (Become) (L19)
- [x] 普通形 (Plain Form) (L20)

### 第五部分：从句与逻辑 (L21-L25)
- [x] ～と思います (Opinion) (L21)
- [x] ～と言います (Quote) (L21)
- [x] 名詞修飾 (Noun Modification) (L22)
- [x] ～とき (When) (L23)
- [x] ～と (Conditional - Machine/Nature) (L23)
- [x] ～くれます (Give to me) (L24)
- [x] ～たら (Conditional) (L25)
- [x] ～ても (Even if) (L25)

### 第六部分：重要补充文法 (Essential Supplements)
> 根据 N5 实战与进阶需求补充

**A. 原因与转折 (中级逻辑连接)**
- [x] ～から (Reason) (L9/L28): 主观原因，与「～て」（原因）的区分。
- [x] ～が (Contrast) (L8): 逆接连接词（但是...）。

**B. 授受动词进阶 (Advanced Giving/Receiving)**
- [x] ～てあげます (Do favor for someone) (L24)
- [x] ～てもらいます (Receive favor) (L24)
- [x] ～てくれます (Do favor for me) (L24)

**C. 疑问词全面掌握 (Wh-Questions Mastery)**
- [x] 疑問詞 + も + 否定 (Complete negation): 何も、誰も、どこも等。
- [x] 基础疑问词对比: いつ / どこ / だれ / どの / どちら。

**D. 特殊名词修饰 (Special Modification)**
- [x] ～という + 名詞 (Named...): 例如「サクラ」という名前。
