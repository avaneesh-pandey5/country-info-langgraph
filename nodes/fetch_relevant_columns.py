def fetch_relevant_columns(state):
    print("--" * 20)
    print("Current Node: fetch_relevant_columns")
    relevant_data = {}
    valid_keys_by_llm = False

    keys = state.get("intent_llm_response", {}).get("keys")
    response = state.get("api_call_response")

    if not response:
        return {"relevant_data": None}

    for index, element in enumerate(response):
        relevant_data[index] = {}
        value = element

        for key in keys:
            try:
                for part in key.split("."):
                    value = value[part]

                relevant_data[index][key] = value
                valid_keys_by_llm = True

            except:
                relevant_data[index][key] = None
        
        relevant_data[index]["name.common"] = element.get("name", {}).get("common")
        relevant_data[index]["name.official"] = element.get("name", {}).get("official")

    return {"relevant_data": relevant_data, "valid_keys_by_llm": valid_keys_by_llm}