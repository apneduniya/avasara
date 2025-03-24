import json


def pretty_json(data: str | bytes | bytearray | list | dict) -> str:
    try:
        if isinstance(data, (str, bytes, bytearray)):
            parsed = json.loads(data)
        else:
            parsed = data
        return json.dumps(parsed, indent=4, sort_keys=True)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


