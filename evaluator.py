def evaluate_health(api, previous_state, success):
    """
    Decide new health state based on previous state and latest result
    """

    current_state = previous_state["current_state"]
    consecutive_failures = previous_state["consecutive_failures"]
    threshold = api["failure_threshold"]

    if success:
        # Reset failures on success
        consecutive_failures = 0
        new_state = "HEALTHY"
    else:
        consecutive_failures += 1
        if consecutive_failures >= threshold:
            new_state = "UNHEALTHY"
        else:
            new_state = "DEGRADED"

    state_changed = new_state != current_state

    return {
        "new_state": new_state,
        "consecutive_failures": consecutive_failures,
        "state_changed": state_changed
    }
