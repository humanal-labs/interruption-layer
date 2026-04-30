def should_stop(action, confidence, history):
    risky_keywords = ["delete", "rm", "drop", "prod", "deploy", "overwrite"]

    if any(k in action.lower() for k in risky_keywords):
        if confidence < 0.6:
            return True, f"Low confidence ({confidence}) on risky action"

    if len(history) >= 3 and len(set(history[-3:])) == 1:
        return True, "Loop detected"

    return False, ""
