from langgraph.graph import StateGraph
import dotenv
from state import State

from nodes.start_node import start_node
from nodes.intent_detection import intent_detection
from nodes.api_calling import api_calling
from nodes.fetch_relevant_columns import fetch_relevant_columns
from nodes.fetch_relevant_keys_from_response import fetch_relevant_keys_from_response
from nodes.humanized_response import humanized_response
from nodes.end_node import end_node

from conditions.call_api_condition import call_api_condition
from conditions.fetch_relevant_data_condition import fetch_relevant_data_condition
from conditions.humanized_response_condition import humanized_response_condition

dotenv.load_dotenv()

workflow = StateGraph(State)

workflow.add_node("start",start_node)
workflow.add_node("intent_detection",intent_detection)
workflow.add_node("api_calling",api_calling)
workflow.add_node("fetch_relevant_columns",fetch_relevant_columns)
workflow.add_node("fetch_relevant_keys_from_response",fetch_relevant_keys_from_response)
workflow.add_node("humanized_response",humanized_response)
workflow.add_node("end_node",end_node)

workflow.set_entry_point("start")

workflow.add_edge("start","intent_detection")
workflow.add_conditional_edges("intent_detection",call_api_condition)
workflow.add_conditional_edges("api_calling",fetch_relevant_data_condition)
workflow.add_conditional_edges("fetch_relevant_columns",humanized_response_condition)
workflow.add_edge("fetch_relevant_keys_from_response","intent_detection")
workflow.add_edge("humanized_response","end_node")

app = workflow.compile()

initial_state = {
    "llm_model_name" : "",
    "question_from_user" : "",
    "intent_llm_response":{},
    "api_call_response" : {},
    "api_call_success_code":0,
    "relevant_data":{},
    "valid_keys_by_llm": False,
    "all_keys_from_response": [],
    "humanized_answer": {},
    "passed_relevent_keys_to_intent": False
}

final_state = app.invoke(initial_state)

print("Final Answer: ", final_state["humanized_answer"])