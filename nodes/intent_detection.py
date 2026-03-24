from prompt import intent_detection_llm_prompt
from langchain_openai import ChatOpenAI
from helper import parse_llm_json

def intent_detection(state):
    print("--" * 20)
    print("Current Node: intent_detection")
    if state["all_keys_from_response"] != []:
        prompt = intent_detection_llm_prompt(question_from_user = state["question_from_user"],available_keys = state["all_keys_from_response"])
    else:
        prompt = intent_detection_llm_prompt(question_from_user = state["question_from_user"])
    llm = ChatOpenAI(model = state["llm_model_name"])
    response = llm.invoke(prompt)
    response = parse_llm_json(response.content)
    return {"intent_llm_response":response}