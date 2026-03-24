def start_node(state):
    """This node will initialize the state with values"""
    print("Starting the workflow...")
    print("--" * 20)
    print("Current Node: start_node")
    question = "What is the currency for India?"
    llm_model = "gpt-4o-mini"

    return {
        "llm_model_name": llm_model,
        "question_from_user": question
    }