import streamlit as st
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROPOSED_FLOWCHART = ROOT / "flow chart.png"
LANGGRAPH_FLOWCHART = ROOT / "flow chart langgraph.png"


def render_about_page():
    st.title("About")
    st.write(
        "This project is a LangGraph-based country information agent that detects user intent, "
        "queries the REST Countries API, and returns a short answer generated from the relevant data."
    )

    st.subheader("Workflow Diagrams")
    col1, col2 = st.columns(2)

    with col1:
        st.image(str(PROPOSED_FLOWCHART), caption="Proposed flow chart drawn by hand", use_container_width=True)

    with col2:
        st.image(str(LANGGRAPH_FLOWCHART), caption="Current LangGraph workflow", use_container_width=True)

    st.subheader("How It Works")
    st.markdown(
        """
1. `start` initializes the workflow state and selects the LLM model.
2. `intent_detection` identifies the country and the relevant response keys.
3. `call_api_condition` decides whether the workflow should call the API or stop.
4. `api_calling` queries the REST Countries API.
5. `fetch_relevant_data_condition` routes the workflow based on the API result.
6. `fetch_relevant_columns` extracts only the fields needed for the answer.
7. `humanized_response_condition` either continues, retries with derived keys, or stops.
8. `fetch_relevant_keys_from_response` gathers all available keys when a retry is needed.
9. `humanized_response` generates the final natural-language answer.
10. `end_node` returns the final output or a fallback message.
        """
    )

    st.subheader("Run")
    st.code("streamlit run app.py", language="bash")
