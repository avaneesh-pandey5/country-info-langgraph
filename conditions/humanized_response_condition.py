from typing import Literal

def humanized_response_condition(state) -> Literal["humanized_response", "fetch_relevant_keys_from_response", "end_node"]:
    print("--" * 20)
    print("Current Node: humanized_response_condition")
    if state["valid_keys_by_llm"]:
        return "humanized_response"
    
    if state["passed_relevent_keys_to_intent"]:
        return "end_node"
    return "fetch_relevant_keys_from_response"