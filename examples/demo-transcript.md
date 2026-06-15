# Demo Transcript

## Request

```json
{
  "subject": "概率论与数理统计",
  "task": "diagnose_student_attempt",
  "workspace_path": "/path/to/course-materials/probability",
  "question": "设 X1,...,Xn 来自 U(0,theta)，求 theta 的最大似然估计，并判断相合性。",
  "student_attempt": "L(theta)=1/theta^n，所以 theta 越小越好，theta_hat=样本均值。",
  "constraints": {
    "language": "zh-CN",
    "time_budget_minutes": 8
  }
}
```

## Skill Response

```json
{
  "source_basis": [
    "概率论/概率论期末解题系统.md"
  ],
  "task_mode": "diagnose_student_attempt",
  "question_type": "T7 参数估计题",
  "operator_chain": [
    "O20 最大似然估计",
    "O21 无偏性与相合性算子"
  ],
  "answer": "本题是支持集依赖参数的最大似然题。联合密度为 L(theta)=theta^{-n} I(theta >= X_(n))，其中 X_(n)=max X_i。因为 theta^{-n} 随 theta 增大而减小，所以在约束 theta >= X_(n) 下取最小允许值，故 MLE 为 theta_hat=X_(n)。相合性：P(|X_(n)-theta|>epsilon)=P(X_(n)<theta-epsilon)=((theta-epsilon)/theta)^n -> 0，因此 X_(n) 依概率收敛到 theta。",
  "diagnosis": [
    "算子误调",
    "步骤缺口"
  ],
  "next_drills": [
    "做 3 道支持集含参数的 MLE：U(0,theta)、U(theta,theta+1)、Pareto 下界参数。",
    "每题必须先写参数约束，再判断似然函数单调性。",
    "闭卷复述：为什么本题不是矩估计，为什么均值不是 MLE。"
  ]
}
```

## What The Agent Learned

- The student's main failure was not algebra but a missing support constraint.
- The reinforcement set targets `O20` only, instead of adding unrelated probability drills.
- The answer is directly writable on an exam page.
