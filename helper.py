import json
import ast
import re

# Helper Functions

def get_keys(data, prefix=""):
    keys = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{prefix}.{key}" if prefix else key
            keys.append(full_key)
            keys.extend(get_keys(value, full_key))
    
    elif isinstance(data, list):
        for index, item in enumerate(data):
            full_key = f"{prefix}[{index}]"
            keys.extend(get_keys(item, full_key))
    
    return keys

def parse_llm_json(raw: str):
    """
    Robust parser for LLM JSON outputs.
    - Tries direct json.loads
    - If fails, tries ast.literal_eval for Python-like dicts
    - If still fails, tries to extract JSON block via regex
    - Cleans common LLM JSON issues (trailing commas, stray text)
    """
    if raw is None:
        raise ValueError("LLM returned None")

    raw = raw.strip()

    # Try direct JSON load
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Try parsing as Python literal (e.g., single-quoted dict)
    try:
        return ast.literal_eval(raw)
    except (ValueError, SyntaxError):
        pass

    # Attempt to extract JSON substring
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if match:
        json_str = match.group()

        # Fix common issues
        json_str = re.sub(r',\s*}', '}', json_str)
        json_str = re.sub(r',\s*]', ']', json_str)

        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            try:
                return ast.literal_eval(json_str)
            except (ValueError, SyntaxError):
                pass

    raise ValueError(f"Unable to parse JSON from LLM output:\n{raw}")