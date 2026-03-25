import streamlit as st
from about import render_about_page
from main import app, initial_state

st.set_page_config(page_title="Country Information AI Agent", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])


def render_log(log):
    """Render log based on its type safely."""
    if isinstance(log, dict):
        try:
            st.table(log)
        except Exception:
            st.write(log)
    elif isinstance(log, list):
        for item in log:
            render_log(item)
    elif isinstance(log, (str, int, float, bool)):
        st.write(log)
    elif log is None:
        st.write("None")
    else:
        st.write(str(log))


if page == "Home":
    st.title("Country Detail Agent using LangGraph")

    question = st.text_input("Enter your question:")

    if st.button("Run Workflow") and question.strip() != "":
        state = initial_state.copy()
        state["question_from_user"] = question

        final_state = app.invoke(state)
        logs = final_state.get("logs", [])

        if not logs:
            st.write("No state logs")
        else:
            for log in logs:
                render_log(log)

elif page == "About":
    render_about_page()
