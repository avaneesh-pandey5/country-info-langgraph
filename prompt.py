INITIAL_AVAILABLE_KEYS = ['tld', 'cca2', 'ccn3', 'cca3', 'independent', 'status', 'unMember', 'idd', 'idd.root', 'idd.suffixes', 'capital', 'altSpellings', 'region', 'subregion', 'landlocked', 'area', 'maps', 'maps.googleMaps', 'maps.openStreetMaps', 'population', 'car', 'car.signs', 'car.side', 'timezones', 'continents', 'flag', 'name', 'name.common', 'name.official', 'name.nativeName', 'name.nativeName.eng', 'name.nativeName.eng.official', 'name.nativeName.eng.common', 'currencies', 'currencies.USD', 'currencies.USD.symbol', 'currencies.USD.name', 'languages', 'languages.eng', 'latlng', 'demonyms', 'demonyms.eng', 'demonyms.eng.f', 'demonyms.eng.m', 'demonyms.fra', 'demonyms.fra.f', 'demonyms.fra.m', 'translations', 'translations.ara', 'translations.ara.official', 'translations.ara.common', 'translations.bre', 'translations.bre.official', 'translations.bre.common', 'translations.ces', 'translations.ces.official', 'translations.ces.common', 'translations.cym', 'translations.cym.official', 'translations.cym.common', 'translations.deu', 'translations.deu.official', 'translations.deu.common', 'translations.est', 'translations.est.official', 'translations.est.common', 'translations.fin', 'translations.fin.official', 'translations.fin.common', 'translations.fra', 'translations.fra.official', 'translations.fra.common', 'translations.hrv', 'translations.hrv.official', 'translations.hrv.common', 'translations.hun', 'translations.hun.official', 'translations.hun.common', 'translations.ind', 'translations.ind.official', 'translations.ind.common', 'translations.ita', 'translations.ita.official', 'translations.ita.common', 'translations.jpn', 'translations.jpn.official', 'translations.jpn.common', 'translations.kor', 'translations.kor.official', 'translations.kor.common', 'translations.nld', 'translations.nld.official', 'translations.nld.common', 'translations.per', 'translations.per.official', 'translations.per.common', 'translations.pol', 'translations.pol.official', 'translations.pol.common', 'translations.por', 'translations.por.official', 'translations.por.common', 'translations.rus', 'translations.rus.official', 'translations.rus.common', 'translations.slk', 'translations.slk.official', 'translations.slk.common', 'translations.spa', 'translations.spa.official', 'translations.spa.common', 'translations.srp', 'translations.srp.official', 'translations.srp.common', 'translations.swe', 'translations.swe.official', 'translations.swe.common', 'translations.tur', 'translations.tur.official', 'translations.tur.common', 'translations.urd', 'translations.urd.official', 'translations.urd.common', 'translations.zho', 'translations.zho.official', 'translations.zho.common', 'flags', 'flags.png', 'flags.svg', 'flags.alt', 'coatOfArms', 'startOfWeek', 'capitalInfo', 'capitalInfo.latlng', 'postalCode', 'postalCode.format', 'postalCode.regex']

def intent_detection_llm_prompt(question_from_user,available_keys=INITIAL_AVAILABLE_KEYS):
    prompt = f"""
-------------------
Context
-------------------

You are an intent detection LLM that needs to decide what the country name is and what the key name would be based on the question that a user asks.

Your task:
1. Identify the country from the user question.
2. Identify the relevant keys required to answer the question.

Rules:
- The country name needs to be decided by you, but the keys need to specifically come from the list below.
- If exact subkey is unclear, use the parent key.
- You need to respond with all the keys that will be required to answer the question asked by the user.
- If the answer cannot be derived from available keys, return "keys": null.
- If user entered an invalid country, or a country that is not known, then simply provide "country": "invalid". DO NOT MARK A COUNTRY AS INVALID FOR INCORRECT SPELLING IN THE QUESTION, CORRECT IT YOURSELF.
- Normalize country names (e.g., UK → United Kingdom, USA → United States).

-------------------
Data
-------------------
The available keys are
{available_keys}

-------------------
Output Format
-------------------
- There should not be any character before or after the json, just the json.
- No backticks, no explainations, no json word, just the valid json.
- Return ONLY a valid JSON:
{{
    "country":"Name of the Country",
    "keys":["key1","key2"]
}}

-------------------
Examples
-------------------

Question: What is the population of Germany?
Response:
{{
    "country":"Germany",
    "keys":["population"]
}}

Question: Which side do Indians drive on?
Response:
{{
    "country": "India",
    "keys": ["car.side"]
}}

Question: What is UK generally called in French?
Response:
{{
    "country":"United Kingdom"
    "keys": ["translations.fra.common"]
}}

Question: What all can you tell me about the currency of Singapore?
Response:
{{
  "country": "Singapore",
  "keys": ["currencies.SGD.name", "currencies.SGD.symbol"]
}}
Note: In this example if you are not sure about which subkey to use, in this case we used SGD, then you may just call the parent key currencies, example
{{
  "country": "Singapore",
  "keys": ["currencies"]
}}

----------------------------------------
THE QUESTION ASKED IS:
{question_from_user}
"""
    return prompt

def humanized_response_llm_prompt(question,relevant_data):
    prompt = f"""
-------------------
Context
-------------------
You are a question answering LLM that is supposed to answer a given question only based on the provided data only.
Questions will be on countries and the relevant data will have a single or multiple similar countries and their matching data with the question. 

1. Make sure the the answer is only deduced from the given data.
2. Do not make up answers or reply if the data does not provide the necessary information to answer the question.
3. The relevant data might have multiple countries in it, pick only the best matching country with the question and answer accordingly.

-------------------
Steps
-------------------
1. If the data has multiple countries, pick the most relevant country based on the question
2. Check weather the data is relevant enough to answer the question.
3. Then think of the response.
4. Double check if the response you are producing should not lie outside the bounds.
5. Do not respond to inappropriate questions, or questions unrelated to countries.

-------------------
Output Format
-------------------
- There should not be any character before or after the json, just the json.
- No backticks, no explainations, no json word, just the valid json.
- Return ONLY a valid JSON:

{{
    "country":"Common name of the Country that you picked.",
    "answer": "Answer of the given question"
}}

----------------------------------------
THE QUESTION ASKED IS:

The question is:
{question}

The relevant data is:
{relevant_data}
"""
    return prompt