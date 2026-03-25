import requests
import json

def api_calling(state):

    logs = state.get("logs", [])
    logs.append("--" * 20)
    logs.append("##### Current Node: **api_calling**")

    api_url = "https://restcountries.com/v3.1/name/{country_name}"
    try:
        api_url = api_url.format(country_name = state["intent_llm_response"]["country"])

        logs.append(f"Calling API: {api_url}")
        
        response = requests.get(api_url)
        response = json.loads(response.content)

        if "message" in response:
            return {"api_call_response":response,"api_call_success_code":response["status"], "logs": logs}
    except:
        return {"api_call_response":{},"api_call_success_code":500, "logs": logs}
    
    return {"api_call_response":response,"api_call_success_code":200, "logs": logs}