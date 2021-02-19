"""Node value converter ."""


def convert(node_value):
    if node_value is None:
        return 'null'
    elif isinstance(node_value, bool):
        return str(node_value).lower()
    return str(node_value)
