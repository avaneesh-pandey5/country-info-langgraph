from helper import get_keys

def fetch_relevant_keys_from_response(state):
    logs = state.get("logs", [])
    logs.append("--" * 20)
    logs.append("##### Current Node: **fetch_relevant_keys_from_response**")

    keys = get_keys(state["api_call_response"])
    return {"all_keys_from_response": keys, "passed_relevent_keys_to_intent": True, "logs": logs}