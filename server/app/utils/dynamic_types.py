import typing as t


def create_literal_type(values: t.List[str]) -> t.Type:
    """Create literal types dynamically for each provider"""
    return t.Literal[tuple(values)] # type: ignore

