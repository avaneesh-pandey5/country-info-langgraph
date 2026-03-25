from typing import TypedDict, List, Optional, Dict, Any

class IntentResponse(TypedDict):
    country: str
    keys: Optional[List[str]]

class HumanizedAnswer(TypedDict):
    country: str
    answer: str

class State:
    logs: List[Any]
    llm_model_name: str
    question_from_user: str
    intent_llm_response: IntentResponse
    api_call_response: Optional[Dict[str, Any]]
    api_call_success_code : int
    relevant_data: Optional[Dict[int, Dict[str, Any]]]
    valid_keys_by_llm: bool
    all_keys_from_response: Optional[List[str]]
    passed_relevent_keys_to_intent: bool
    humanized_answer: HumanizedAnswer
