import time

def should_interrupt(task):
    # Rule 1: destructive commands
    if task["tool"] == "bash" and "rm -rf" in task["cmd"]:
        return True, "Destructive command"

    # Rule 2: low confidence + high cost
    if task["confidence"] < 0.7 and task["cost"] > 500:
        return True, "Low confidence, high cost"

    return False, None


def governor(task):
    interrupt, reason = should_interrupt(task)

    if interrupt:
        print(f"\n⚠️ GOVERNOR TRIGGERED: {reason}")
        print("Pausing for 10 seconds...\n")

        # Simulated pause (can be replaced with human approval)
        time.sleep(3)

        print("Action requires review before execution.\n")
        return False
    else:
        print(f"\n✅ Executed: {task['cmd']} (cost: ${task['cost']})\n")
        return True


# ---- Simulation ---- #

tasks = [
    {"tool": "api", "cmd": "check_inventory", "confidence": 0.95, "cost": 5},
    {"tool": "api", "cmd": "place_order", "confidence": 0.65, "cost": 18000},
    {"tool": "bash", "cmd": "rm -rf /data", "confidence": 0.9, "cost": 0},
    {"tool": "api", "cmd": "update_status", "confidence": 0.98, "cost": 2},
]

print("=== Running Agent Simulation ===\n")

for t in tasks:
    governor(t)

print("\n=== End ===")
