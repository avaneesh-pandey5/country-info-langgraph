from typing import Literal

def fetch_relevant_data_condition(state) -> Literal["fetch_relevant_columns", "intent_detection", "end_node"]:
    print("--" * 20)
    print("Current Node: fetch_relevant_data_condition")
    if state["api_call_success_code"] == 200:
        return "fetch_relevant_columns"
    if state["api_call_success_code"] == 500:
        return "end_node"
    if state["api_call_success_code"]  == 404:
        return "intent_detection"