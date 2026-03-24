from typing import Literal

def call_api_condition(state) -> Literal["api_calling", "end_node"]:
    print("--" * 20)
    print("Current Node: call_api_condition")
    if state["intent_llm_response"]["keys"] != None and state["intent_llm_response"]["country"].lower() != "invalid":
        return "api_calling"
    else:
        return "end_node"