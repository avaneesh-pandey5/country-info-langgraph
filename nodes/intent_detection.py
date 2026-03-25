from prompt import intent_detection_llm_prompt
from langchain_openai import ChatOpenAI
from helper import parse_llm_json

def intent_detection(state):

    logs = state.get("logs", [])
    logs.append("--" * 20)
    logs.append("##### Current Node: **intent_detection**")

    if state["all_keys_from_response"] != []:
        logs.append("We called API with the given country name and passing those keys to the intent detection LLM to get better output")
        prompt = intent_detection_llm_prompt(question_from_user = state["question_from_user"],available_keys = state["all_keys_from_response"])
    else:
        prompt = intent_detection_llm_prompt(question_from_user = state["question_from_user"])
    llm = ChatOpenAI(model = state["llm_model_name"])
    response = llm.invoke(prompt)
    response = parse_llm_json(response.content)

    logs.append("Intent Detection LLM response:")
    logs.append(response)
    
    return {"intent_llm_response":response, "logs": logs}