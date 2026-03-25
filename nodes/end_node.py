def end_node(state):

    # we'll decide which node got us to end node and based on that we'll decide what to return as the final output of the workflow

    logs = state.get("logs", [])
    logs.append("--" * 20)
    logs.append("##### Current Node: **end_node**")

    if state["intent_llm_response"]["country"] == "invalid":
        logs.append("Please enter a valid country name in your question. Ending the workflow without calling the API.")
        return {"logs": logs, "humanized_answer": {"answer": "Sorry, I couldn't identify a valid country name in your question. Please try asking with a valid country name."}}
    if state["intent_llm_response"]["keys"] == None:
        logs.append("Intent detection LLM couldn't find any relevant keys based on the question asked.")
        logs.append("Ending the workflow without calling the API as we don't have any relevant data to fetch based on the user's question.")
        return {"logs": logs, "humanized_answer": {"answer": "Sorry, I couldn't find any relevant information based on your question. Please try asking in a different way or provide more details."}}
    if state["api_call_success_code"] == 500:
        logs.append("API call failed due to some error. Ending the workflow without fetching any relevant data.")
        return {"logs": logs, "humanized_answer": {"answer": "Sorry, there was an error while fetching the data. Please try again later."}}
    if not state["valid_keys_by_llm"] and state["passed_relevent_keys_to_intent"]:
        logs.append("We have already passed the relevant keys to intent detection LLM and still couldn't get any valid keys. So, ending the workflow without fetching any relevant data.")
        return {"logs": logs, "humanized_answer": {"answer": "Sorry, I couldn't find any relevant information based on your question even after analyzing the API response and retrying. Please try asking in a different way or provide more details."}}
    if state["humanized_answer"]:
        logs.append("Humanized answer generated successfully. Ending the workflow and returning the final answer.")
        logs.append(f"Final Answer is {state["humanized_answer"]["answer"]}")
        return {"logs": logs, "humanized_answer": state["humanized_answer"]}
    
    return state["humanized_answer"]