def get_data_fig(*sides, **kwargs):
    perimeter = sum(sides)

    tp = kwargs.get('tp')
    color = kwargs.get('color')
    closed = kwargs.get('closed')
    width = kwargs.get('width')

    result = (perimeter,)
    if tp is not None:
        result += (tp,)
    if color is not None:
        result += (color,)
    if closed is not None:
        result += (closed,)
    if width is not None:
        result += (width,)

    return result