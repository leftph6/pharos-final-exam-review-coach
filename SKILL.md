---
name: final-exam-review-coach
description: "Use this skill for Chinese final-exam review work across subjects: turning course materials, exam ranges, past papers, homework banks, and prior outputs into subject-specific review plans, operator-level notes, standard answers, mock exams, Q&A explanations, weak-point diagnosis, and reinforcement loops."
metadata:
  version: "1.1.0"
  category: education
---

# Final Exam Review Coach

## Purpose

Guide each subject's exam preparation as a closed loop:

1. align sources to the exam,
2. compress knowledge into reusable operators,
3. answer questions in exam-standard form,
4. diagnose weak points by operator,
5. reinforce with targeted drills and mock papers.

When working with an existing course-material workspace, read `references/workspace-subject-index.md` first if present to understand the expected folder conventions and artifact patterns.

## Agent Carnival Fit

This is a standardized Skill module for education agents. It performs reusable content-generation and assessment tasks that a larger Agent can call:

- read a course corpus and infer an exam profile;
- compress chapters, slides, past papers, and homework banks into operator-level knowledge;
- answer student questions with an operator chain and exam-standard wording;
- diagnose weak points from a student's attempted solution;
- generate targeted drills, mock papers, and final cram sheets.

It is intentionally domain-adaptive: the same interface works for math, finance, DSP, PDE, data structures, probability, accounting/economics, and language exams. In a Pharos Agent Arena build, it can be composed with wallet/payment/credential Skills to issue study bounties, proof-of-progress credentials, or tutor payment flows, but this Skill itself does not require private keys or transaction authority.

## Callable Actions

Use these action names when wrapping the Skill for an agent runtime:

- `build_subject_profile`: map sources, exam date/range, likely question slots, and existing outputs.
- `compress_exam_portrait`: produce `T1/T2/...` question taxonomy with evidence.
- `build_operator_library`: produce `O/OP` operators with trigger, input, operation, output, example, pitfalls.
- `answer_exam_question`: solve one question with type recognition, operator chain, and standard answer.
- `diagnose_student_attempt`: classify mistakes by operator and failure mode.
- `generate_reinforcement_pack`: create targeted drills, mock paper, answer key, and last-day checklist.

### Input Contract

```json
{
  "subject": "金融数学",
  "task": "answer_exam_question",
  "workspace_path": "/absolute/path/to/course/materials",
  "materials": ["optional explicit files or folders"],
  "question": "optional student question or exam item",
  "student_attempt": "optional answer draft for diagnosis",
  "constraints": {
    "language": "zh-CN",
    "time_budget_minutes": 15,
    "exam_date": "2026-06-16"
  }
}
```

### Output Contract

```json
{
  "source_basis": ["files or evidence used"],
  "task_mode": "answer_exam_question",
  "question_type": "T3 债券久期题",
  "operator_chain": ["O10 债券定价", "O12 Macaulay 久期"],
  "answer": "exam-ready explanation or artifact path",
  "diagnosis": ["optional weak-point labels"],
  "next_drills": ["optional targeted reinforcement items"]
}
```

## First Move

When a user names a subject or asks for review help:

1. Locate the subject folder and existing outputs. Prefer `rg --files` and read file names before opening large PDFs.
2. Identify the authoritative inputs: exam range, recent schedule, teacher slides, textbook chapters, past papers, homework/question bank, and already generated notes.
3. State the working mode briefly: Q&A, operator-note building, standard-answer drafting, mock-exam generation, weak-point diagnosis, or schedule planning.
4. If the exam date or range matters, verify it from local schedule/range files before planning.

Do not start by summarizing all materials. Build the smallest context needed for the user's current subject and task.

## Core Workflow

### 1. Subject Profile

Create a compact profile before doing substantial work:

- exam date/time and remaining days if available;
- source priority: exam range > teacher materials > past papers/homework > textbook > external/general knowledge;
- existing outputs to reuse;
- main question slots or chapter blocks;
- high-risk topics, missing materials, and likely scoring structure.

For calculation-heavy subjects, include formula families and standard steps. For concept-heavy subjects, include definition keywords, comparison pairs, and short-answer templates. For language subjects, include grammar operators, particles, sentence patterns, vocabulary, and transformation drills.

### 2. Exam-Portrait Compression

Infer the exam portrait from past papers, mock papers, homework, and teacher ranges:

- `T1/T2/...` for question types or paper slots;
- source evidence for each slot;
- expected output form: proof, calculation, derivation, short answer, code/pseudocode, translation, fill-in, multiple choice;
- time budget and points if visible;
- common traps and easy-lost steps.

If evidence is weak, mark it as inference instead of certainty.

### 3. Operator-Level Notes

Compress every recurring move into an operator. Use this schema:

```text
O#: operator name
Trigger: how to recognize the problem
Input: known quantities / conditions / text cues
Operation: formulas, transformations, proof steps, or grammar rules
Output: what the answer must produce
Exam wording: a short writeable version
Example: one minimal worked example
Pitfalls: common mistakes and how to avoid them
```

The user's prior successful pattern is `input -> operation -> output`, not generic explanation. Keep operators callable during Q&A and mock grading.

### 4. Standard Answers

For any exercise, mock paper, homework bank, or past paper:

1. classify the question type;
2. name the operator chain;
3. solve in clean exam-writing order;
4. show essential formulas and substitutions;
5. end with the final result or conclusion;
6. add a short "scoring points / lost-point risks" note when useful.

For proof questions, separate assumptions, target, construction, and conclusion. For programming/data-structure questions, include invariant, complexity, and edge cases. For finance/accounting questions, define variables and units.

### 5. Q&A Mode

When answering a student's question:

- first identify the problem type and relevant operators;
- explain the shortest path to the answer;
- include the full derivation only when the question needs it;
- give a "next similar drill" if the user is practicing;
- if the user is confused, diagnose whether the block is in reading the question, choosing an operator, executing the steps, algebra/arithmetic, memory, or speed.

Avoid broad lectures. Make the answer usable on the exam page.

### 6. Weak-Point Diagnosis

Use operator-based diagnosis rather than only right/wrong grading. Ask the student to return this format when drilling:

```text
Q#
题型识别：
算子链：
是否做出：
卡点：
```

Classify mistakes into:

- `识题错误`: did not map the question to the right slot;
- `算子误调`: chose the wrong operator or missed one;
- `步骤缺口`: knew the operator but skipped a required exam step;
- `计算/符号错误`: algebra, units, signs, conditions, notation;
- `表达失分`: result correct but answer not written in a scorable form;
- `速度问题`: correct path but too slow.

Then generate a focused drill set that attacks only the failed operator(s).

### 7. Reinforcement Loop

Use this loop for each subject:

1. `Build`: create or update operator notes and formula/definition sheets.
2. `Recall`: closed-book operator-chain listing and one-page memory sheet.
3. `Apply`: targeted exercises by operator, then mixed exercises by question slot.
4. `Simulate`: timed mock paper with answer key.
5. `Diagnose`: grade by operator and mistake class.
6. `Compress`: produce final cram sheet and last-day checklist.

Stop expanding materials near the exam. In final days, prefer recall, standard answer templates, and old mistakes.

## Deliverable Patterns

Use these names and structures when creating new artifacts:

- `科目-期末标准答案与总复习笔记.md/.tex/.pdf`: source note, exam portrait, operator library, standard templates, high-risk points, final cram version.
- `科目-期末模拟题与参考答案.md/.tex/.pdf`: exam-like paper first, answer key after, with operator tags.
- `科目-算子级别笔记.md/.tex/.pdf`: minimal concept definitions plus operator library.
- `薄弱点诊断-第N轮.md`: closed-book diagnostic paper with target operators and return format.
- `新版考试安排-复习时间表.md`: schedule, priorities, daily focus, and current bottlenecks.

Keep Markdown as the editable source unless the user needs TeX/PDF.

## Subject Adaptation

- Math/finance/numerical/DSP/PDE: emphasize formulas, derivations, stability/condition checks, units, and final result formatting.
- Probability/statistics: build a minimal `T` question taxonomy and `O` operator library; every answer starts with distribution/region/estimator recognition.
- Data structures: focus on operations, hand-written algorithms, invariants, complexity, and trace tables.
- Optimal control/modeling: use Euler-Lagrange, transversality, Pontryagin, bang-bang, and dynamic programming templates.
- Finance/accounting/economics: separate definitions, formulas, calculation procedures, comparison tables, and short-answer wording.
- Japanese/language: use grammar-pattern operators, particle contrasts, question-answer assembly tables, vocabulary transformations, and sentence templates.

## Quality Bar

Before delivering, check:

- the source basis is named;
- every major topic maps to either a question type or an operator;
- formulas define variables and conditions;
- standard answers are directly writeable;
- weak-point drills target specific operators;
- no large new study burden is introduced without exam value.
