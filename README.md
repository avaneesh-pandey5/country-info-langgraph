# Country Information AI Agent

A LangGraph-based country question-answering agent that:

- detects the country and required data fields from a user question,
- fetches country data from the REST Countries API,
- extracts only the relevant fields,
- generates a short natural-language answer using an OpenAI model,
- exposes the workflow through a Streamlit UI with step-by-step logs.

## Flow Chart

<table>
  <tr>
    <td align="center">
      <img src="./flow%20chart.png" alt="Proposed flow chart drawn by hand" width="450"><br>
      <sub>Proposed flow chart drawn by hand</sub>
    </td>
    <td align="center">
      <img src="./flow%20chart%20langgraph.png" alt="Flow chart generated from current LangGraph workflow" width="450"><br>
      <sub>Current LangGraph workflow</sub>
    </td>
  </tr>
</table>

## How It Works

The app is currently live [here](https://country-info-langgraph.streamlit.app/) 


The workflow is defined in `main.py` using LangGraph.

### Main Nodes

1. `start`  
   Initializes the workflow state and selects the LLM model.
2. `intent_detection`  
   Uses the LLM to identify:
   - the country mentioned in the question
   - the relevant REST Countries response keys needed to answer it
3. `api_calling`  
   Calls `https://restcountries.com/v3.1/name/{country_name}`.
4. `fetch_relevant_columns`  
   Extracts the requested fields from the API response.
5. `fetch_relevant_keys_from_response`  
   If the first set of keys is not usable, the workflow derives all available keys from the API payload and retries intent detection.
6. `humanized_response`  
   Uses the LLM again to turn the extracted data into a short answer.
7. `end_node`  
   Returns the final answer or a fallback error message.

### Conditional Nodes

1. `call_api_condition`  
   Runs after `intent_detection` and decides whether to continue to `api_calling` or stop at `end_node`.
2. `fetch_relevant_data_condition`  
   Runs after `api_calling` and routes the workflow based on API status:
   - `200` -> `fetch_relevant_columns`
   - `404` -> `intent_detection`
   - `500` -> `end_node`
3. `humanized_response_condition`  
   Runs after `fetch_relevant_columns` and decides whether to:
   - continue to `humanized_response`
   - retry via `fetch_relevant_keys_from_response`
   - stop at `end_node`

## Project Structure

```text
.
├── app.py                   # Streamlit UI
├── main.py                  # LangGraph workflow definition
├── state.py                 # Shared workflow state
├── prompt.py                # LLM prompts
├── helper.py                # JSON parsing and key extraction helpers
├── nodes/                   # LangGraph nodes
├── conditions/              # Conditional routing functions
├── requirements.txt         # Python dependencies
└── flow chart.png           # Workflow diagram
```

## Requirements

- Python 3.10+
- An OpenAI API key

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

`main.py` loads environment variables with `dotenv.load_dotenv()`, and the LangChain OpenAI client reads `OPENAI_API_KEY`.

## Run The App

Start the Streamlit interface:

```bash
streamlit run app.py
```

Then open the local Streamlit URL in your browser, enter a country-related question, and run the workflow.

## Example Questions

- `What is the population of Germany?`
- `Which side do people drive on in India?`
- `What is the capital of Japan?`
- `What currency is used in Singapore?`
- `What is the French common translation for the United Kingdom?`

## Notes

- The UI in `app.py` shows workflow logs rather than only the final answer.
- The default model is currently set in `nodes/start_node.py` as `gpt-4o-mini`.
- The project depends on the REST Countries API being available.
