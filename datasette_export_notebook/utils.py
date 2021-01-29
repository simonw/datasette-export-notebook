def detect_types(rows):
    """
    Returns {colname: string_type} for these rows, where
    string_type is one of "int", "str" or "float"
    """
    columns = {}
    for row in rows:
        for column, value in dict(row).items():
            if value is not None:
                columns.setdefault(column, set()).add(type(value).__name__)

    # Only suggest type if column had just that type (or that + null)
    suggestions = {}
    for column, types in columns.items():
        if len(types) == 1:
            suggestions[column] = list(types)[0]

    return suggestions
