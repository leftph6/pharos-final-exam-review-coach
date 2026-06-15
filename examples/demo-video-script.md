# Demo Video Script

Length target: 90 seconds.

1. Show the repository root: `SKILL.md`, `schemas/`, `examples/`, `tests/`.
2. Say: "This is Final Exam Review Coach, a standardized education Skill for Pharos agents."
3. Open `SKILL.md` and highlight the callable actions.
4. Run:

   ```bash
   python3 tests/validate_skill_package.py
   ```

5. Open `examples/demo-transcript.md`.
6. Show the request: a probability/statistics MLE diagnosis.
7. Show the response: source basis, question type, operator chain, diagnosis, next drills.
8. Say: "Unlike a normal chatbot answer, this Skill returns the operator chain and the next reinforcement loop, so another agent can schedule study bounties, payments, or credentials on Pharos."
9. End on the Pharos alignment section in `README.md`.
