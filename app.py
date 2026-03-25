import streamlit as st
import io
import sys
from main import app, initial_state

st.set_page_config(page_title="LangGraph Debug UI")

st.title("Country Detail Agent using LangGraph")

question = st.text_input("Enter your question:")

def render_log(log):
    """Render log based on its type safely"""
    if isinstance(log, dict):
        try:
            st.table(log)
        except:
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
if st.button("Run Workflow") and question.strip() != "":
    state = initial_state.copy()
    state["question_from_user"] = question

    final_state = app.invoke(state)

    sys.stdout = sys.__stdout__

    logs = final_state.get("logs", [])

    if not logs:
        st.write("No state logs")
    else:
        for i, log in enumerate(logs):
            render_log(log)
