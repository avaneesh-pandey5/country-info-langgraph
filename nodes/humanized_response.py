from prompt import humanized_response_llm_prompt
from langchain_openai import ChatOpenAI
from helper import parse_llm_json

def humanized_response(state):

    logs = state.get("logs", [])
    logs.append("--" * 20)
    logs.append("##### Current Node: **humanized_response**")

    prompt = humanized_response_llm_prompt(question=state["question_from_user"],relevant_data=state["relevant_data"])
    llm = ChatOpenAI(model = state["llm_model_name"])
    response = llm.invoke(prompt)
    response = parse_llm_json(response.content)
    logs.append("Humanized Response LLM response:")
    logs.append(response)
    return {"humanized_answer":response, "logs": logs}