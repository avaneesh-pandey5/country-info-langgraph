def fetch_relevant_columns(state):

    logs = state.get("logs", [])
    logs.append("--" * 20)
    logs.append("##### Current Node: **fetch_relevant_columns**")

    relevant_data = {}
    valid_keys_by_llm = False

    keys = state.get("intent_llm_response", {}).get("keys")
    response = state.get("api_call_response")

    if not response:
        return {"relevant_data": None}

    for index, element in enumerate(response):
        relevant_data[index] = {}
        
        for key in keys:
            try:
                value = element
                for part in key.split("."):
                    value = value[part]

                relevant_data[index][key] = value
                valid_keys_by_llm = True

            except:
                relevant_data[index][key] = None
        
        relevant_data[index]["name.common"] = element.get("name", {}).get("common")
        relevant_data[index]["name.official"] = element.get("name", {}).get("official")
        
    logs.append("Relevant data fetched based on the keys identified by the intent detection LLM")
    logs.append(relevant_data)
    return {"relevant_data": relevant_data, "valid_keys_by_llm": valid_keys_by_llm, "logs": logs}