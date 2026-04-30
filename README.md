# interruption-layer

LLMs don’t know when they’re out of distribution.

Interruption Layer is a simple guard that blocks risky agent actions before execution.

This is a minimal demonstration — not a full solution.

## What it does

- Blocks low-confidence risky actions
- Detects repeated action loops

## Why this matters

Agentic systems scale decisions.  
Interruption Layers scale judgment.

## Run

```bash
python demo.py
