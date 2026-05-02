from interruption import should_stop

history = []

def run_action(action, confidence):
    stop, reason = should_stop(action, confidence, history)

    if stop:
        print(f"[INTERRUPTED] {reason}")
        print(f"  action: {action}")
        print()
    else:
        print(f"[EXECUTED] {action}")
        history.append(action)
        print()

print("Interruption Layer Demo")
print("-----------------------")

print("Case 1: Safe action")
run_action("ls", 0.9)

print("Case 2: Low-confidence risky shell command")
run_action("rm -rf /", 0.4)

print("Case 3: Dangerous SQL")
run_action("DELETE FROM users;", 0.9)

print("Case 4: Repeated loop")
run_action("retry deploy", 0.9)
run_action("retry deploy", 0.9)
run_action("retry deploy", 0.9)
run_action("retry deploy", 0.9)

print("Summary")
print("-------")
print("Agents can execute before humans can react.")
print("This layer interrupts risky actions before they run.")
