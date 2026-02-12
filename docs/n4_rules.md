# Anki 卡片生成约束规范 (Generation Constraints) - N4 Level

为了保持 N4 文法卡片的一致性和高质量，所有新卡片的生成必须遵循以下约束。

## 1. 核心约束 (Core Constraints)

*   **目标级别**: JLPT N4 (参考《大家的日语》进阶1 L26-L50)
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
    *   正确: `<ruby>会議<rt>かいぎ</rt></ruby>`

### B. 例句设计 (Sentence Design)
*   **简单句**: 侧重展示接续和基本用法。
*   **难句**: 结合 N4 常见场景（职场初步、旅行麻烦处理、更复杂的日常交流），包含从句或复合句。

## 3. N4 完整文法大纲 (Syllabus)

### 第一部分：状态与意向 (L26-L31)
- [ ] ～んです (Explanation) (L26)
- [ ] ～ていただけませんか (Polite Request) (L26)
- [ ] 可能動詞 (Potential Form) (L27)
- [ ] ～しか～ません (Only) (L27)
- [ ] ～ながら (Simultaneous Action) (L28)
- [ ] ～し、～し (Listing Reasons) (L28)
- [ ] ～ています (State of Intransitive Verbs) (L29)
- [ ] ～てしまいます (Completion/Regret) (L29)
- [ ] ～てあります (Result of Action) (L30)
- [ ] ～ておきます (Preparation) (L30)
- [ ] 意向形 (Volitional Form) (L31)
- [ ] ～ようと思っています (Intention) (L31)
- [ ] ～つもりです (Plan) (L31)

### 第二部分：推测、命令与条件 (L32-L35)
- [ ] ～ほうがいいです (Advice) (L32)
- [ ] ～でしょう / ～かもしれません (Probability) (L32)
- [ ] 命令形 / 禁止形 (Imperative/Prohibitive) (L33)
- [ ] ～と書いてあります / ～と読みます (Written info) (L33)
- [ ] ～とおりに (As/Following) (L34)
- [ ] ～あとで (After) (L34)
- [ ] ～ないで (Without doing) (L34)
- [ ] 条件形 (ば形) (Conditional) (L35)
- [ ] ～なら (Conditional - Context) (L35)

### 第三部分：变化、被动与名物化 (L36-L40)
- [ ] ～ように (Aim/Change of state) (L36)
- [ ] ～ようになります (Change of ability) (L36)
- [ ] 受身動詞 (Passive Voice) (L37)
- [ ] ～のは/のが/のを (Nominalization) (L38)
- [ ] ～て / ～ので (Reason - Objective) (L39)
- [ ] 疑問詞＋か (Embedded Question) (L40)
- [ ] ～てみます (Try doing) (L40)

### 第四部分：授受、目的与推测 (L41-L45)
- [ ] ～やります / いただけます / くださいます (Honorific Giving/Receiving) (L41)
- [ ] ～ために (Purpose/Benefit) (L42)
- [ ] ～のに (Usage/Purpose) (L42)
- [ ] ～そうです (Look like/Seem) (L43)
- [ ] ～て来ます (Go and come back) (L43)
- [ ] ～すぎます (Too much) (L44)
- [ ] ～やすい / ～にくい (Easy/Hard to do) (L44)
- [ ] ～場合は (In case of) (L45)
- [ ] ～のに (Although/Regret) (L45)

### 第五部分：高级表达与敬语 (L46-L50)
- [ ] ～ところです (Point in time) (L46)
- [ ] ～ばかりです (Just finished) (L46)
- [ ] ～はずです (Expectation) (L46)
- [ ] ～そうです (Hearsay - I heard that) (L47)
- [ ] ～ようです (Seem/Likelihood) (L47)
- [ ] 使役動詞 (Causative) (L48)
- [ ] 使役受身 (Causative-Passive) (L48)
- [ ] 尊敬語 (Honorifics) (L49)
- [ ] 謙譲語 (Humble) (L50)
