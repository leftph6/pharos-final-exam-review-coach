# Workspace Subject Index

This reference is a portable guide for course-material workspaces. It avoids private local paths and should be adapted by the user or host agent at runtime.

## Expected Workspace Shape

```text
course-materials/
  schedule/
    exam-schedule.xlsx
    review-plan.md
  subject-a/
    exam-range.*
    lecture-slides/
    textbook-notes/
    past-papers/
    homework-bank/
    outputs/
  subject-b/
    ...
```

## Source Priority

Use this order when sources disagree:

1. official exam range and latest schedule;
2. teacher slides, announcements, and handouts;
3. past papers and homework/question banks;
4. existing review outputs created in prior sessions;
5. textbooks and general domain knowledge.

## Recommended Output Names

- `SUBJECT-期末标准答案与总复习笔记.md`
- `SUBJECT-期末模拟题与参考答案.md`
- `SUBJECT-算子级别笔记.md`
- `薄弱点诊断-第N轮.md`
- `复习时间表.md`

## Cross-Subject Patterns

### Math / Finance / Numerical Courses

Use operator notes with:

- formula families;
- variable definitions and units;
- derivation templates;
- stability or condition checks;
- exam-ready final formatting.

### Probability / Statistics

Use a two-layer taxonomy:

- `T1/T2/...`: question slots such as conditional probability, joint density, variable transformation, parameter estimation, confidence interval;
- `O1/O2/...`: reusable operators such as total probability, Bayes, marginal integration, MLE, CLT, pivotal quantity.

Every answer should start with distribution/region/estimator recognition.

### Computer Science / Data Structures

Emphasize:

- operation definitions;
- invariants;
- pseudocode;
- trace tables;
- complexity;
- edge cases.

### Language Courses

Use grammar-pattern operators:

- trigger phrase;
- sentence frame;
- particle or inflection rule;
- common confusion pair;
- minimal example and translation.

### Accounting / Economics / Finance Concepts

Separate:

- definitions;
- formula operators;
- calculation procedure;
- comparison tables;
- short-answer wording;
- confusion traps.

## Reusable Historical Patterns

- Operator notes: `input -> operation -> output`, plus trigger, example, and pitfalls.
- Standard review notes: source basis, exam portrait, operators, answer templates, high-risk loss points, final cram section.
- Mock papers: exam-like questions tagged by operators, then full reference answers.
- Diagnostics: closed-book drills that force the student to write question type, operator chain, whether solved, and stuck point.
- RAG: only for document-heavy subjects; preserve structure-aware chunks by chapter/operator and test retrieval by operator filters.
