import json
from datetime import datetime


def default_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


def pretty_json(data: str | bytes | bytearray | list | dict) -> str:
    try:
        if isinstance(data, (str, bytes, bytearray)):
            parsed = json.loads(data)
        else:
            parsed = data
        return json.dumps(parsed, indent=4, sort_keys=True, default=default_encoder)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


