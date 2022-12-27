def render_to_readable_output(objs):
    """
    This function is not a VIEW. It is just a prettier for output.
    You just need to filter Books and give it to this function.
    """

    splitter = '\n' + ('-' * 70) + '\n\n\n'
    output = splitter.join(map(str, objs))
    return output
