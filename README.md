# Final Exam Review Coach

A standardized education Skill for Pharos/Anvita-style agents that turns messy course materials into exam-ready tutoring workflows: exam portraits, operator-level notes, standard answers, weak-point diagnosis, targeted drills, and mock papers.

## Why This Skill

Most study agents answer one question at a time. This Skill gives an agent a reusable review engine:

- map a subject corpus to likely exam slots;
- compress knowledge into callable `O/OP` operators;
- answer questions with operator chains and scorable wording;
- grade student attempts by failure mode instead of only right/wrong;
- generate the next reinforcement set from the diagnosed weak operators.

It was distilled from a real multi-subject final-exam workspace covering DSP, financial mathematics, PDE numerical methods, data structures, numerical analysis, probability/statistics, optimal control, Japanese, accounting, finance, and economics.

## Pharos Agent Carnival Alignment

Phase 1 asks for standardized Skill modules that agents can call. This repository packages the Skill as a portable module with:

- `SKILL.md`: agent-facing workflow and action definitions;
- `schemas/input.schema.json`: structured request contract;
- `schemas/output.schema.json`: structured response contract;
- `examples/demo-transcript.md`: end-to-end demonstration;
- `tests/validate_skill_package.py`: local validation for required files and schema shape.

This Skill covers the content-generation and data-processing side of an education agent. In Phase 2, it can compose with Pharos wallet/payment/credential Skills to support paid tutoring, study bounties, or proof-of-progress credentials.

## Callable Actions

| Action | Purpose |
|---|---|
| `build_subject_profile` | Find sources, exam range, existing outputs, and high-risk topics. |
| `compress_exam_portrait` | Infer `T1/T2/...` question slots with evidence. |
| `build_operator_library` | Build `O/OP` operators with trigger, input, operation, output, example, pitfalls. |
| `answer_exam_question` | Produce exam-standard answers with operator chains. |
| `diagnose_student_attempt` | Classify mistakes by operator and failure mode. |
| `generate_reinforcement_pack` | Create targeted drills, mock papers, answer keys, and cram sheets. |

## Install

Copy this folder into a Codex skills directory, or invoke the Skill by pointing an agent runtime at `SKILL.md`.

```bash
python3 tests/validate_skill_package.py
```

Expected output:

```text
skill package valid
```

## Minimal Invocation

```json
{
  "subject": "概率论与数理统计",
  "task": "diagnose_student_attempt",
  "workspace_path": "/path/to/course-materials/probability",
  "question": "设 X~U(0,theta)，求 theta 的最大似然估计并判断相合性。",
  "student_attempt": "L(theta)=1/theta^n, theta>Xi, so theta_hat=mean(X).",
  "constraints": {
    "language": "zh-CN",
    "time_budget_minutes": 10
  }
}
```

## Expected Response Shape

```json
{
  "source_basis": ["概率论/概率论期末解题系统.md"],
  "task_mode": "diagnose_student_attempt",
  "question_type": "T7 参数估计题",
  "operator_chain": ["O20 最大似然估计", "O21 相合性"],
  "answer": "The correct MLE is max(X_i), not mean(X_i).",
  "diagnosis": ["算子误调", "步骤缺口"],
  "next_drills": ["Repeat three support-dependent MLE problems."]
}
```

## Differentiators

- Operator-first tutoring: every explanation names the reusable move the student must learn.
- Evidence-aware exam portraits: sources are ranked by exam range, teacher materials, past papers, homework banks, and prior notes.
- Closed-loop reinforcement: diagnose, drill, simulate, compress.
- Cross-subject portability: math, finance, CS, language, accounting, and economics use the same action contract.
- Safe by default: no private keys, no wallet authority, no sensitive submission; on-chain features are delegated to separate Skills.

## Submission Message

Final Exam Review Coach is a reusable education Skill that lets any Pharos agent become an exam-prep specialist. It transforms local course corpora into operator-level knowledge, solves questions in exam-standard form, diagnoses weak points, and generates reinforcement packs. The module is designed for Phase 2 composition with Pharos payment or credential Skills, enabling paid tutoring, study bounties, and proof-of-progress workflows without giving this Skill wallet authority.
