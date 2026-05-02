# Interruption Layer

Stops risky agent actions **before execution**.

Agents are getting better at deciding what to do.

But they still don’t know when **not** to do it.

That’s where things break.

---

## Demo

```bash
$ python demo.py

Interruption Layer Demo
-----------------------

Case 1: Safe action
[EXECUTED] ls

Case 2: Low-confidence risky shell command
[INTERRUPTED] Low confidence (0.4) on risky action
  action: rm -rf /

Case 3: Dangerous SQL
[INTERRUPTED] Dangerous SQL detected
  action: DELETE FROM users;

Case 4: Repeated loop
[EXECUTED] retry deploy
[EXECUTED] retry deploy
[EXECUTED] retry deploy
[INTERRUPTED] Loop detected
  action: retry deploy

Summary
-------
Agents can execute before humans can react.
This layer interrupts risky actions before they run.
What it does

This prototype catches three simple failure modes:

1. Destructive shell commands
    rm -rf / → interrupted
2. Dangerous SQL
    DELETE FROM users; → interrupted
3. Repeated action loops
    same action repeated → interrupted

⸻

Why it matters

Execution is getting cheaper.

The cost of a wrong action is going up.

Agents don’t only suggest anymore.
They can act.

That means safety has to exist before execution, not after damage.

⸻

Core idea

Not smarter agents.

Safer execution.

⸻

Quick start
git clone https://github.com/humanal-labs/interruption-layer
cd interruption-layer
python demo.py
Zero dependencies.

⸻

Status

Early prototype.

Naive rules.
Hardcoded checks.
False positives and false negatives are possible.

Do not use in production.

⸻

Direction

From:

Can the agent do it?

To:

Should the agent be allowed to run it?

This is an early attempt at that missing layer.
