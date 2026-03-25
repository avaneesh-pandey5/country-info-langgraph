def start_node(state):
    """This node will initialize the state with values"""
    logs = []
    logs.append("--" * 20)
    logs.append("##### Current Node: **start_node**")
    
    llm_model = "gpt-4o-mini"
    logs.append(f"LLM Model set to {llm_model}")

    return {
        "llm_model_name": llm_model,
        "logs": logs
    }