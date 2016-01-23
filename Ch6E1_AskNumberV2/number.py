def ask_number(question, step_value):
    """
    Ask a number within a range

    :param question: input question
    :param step_value: A step value
    :return: response after valuating the question
    """

    value = step_value + 5
    response = None
    while response not in range(1, value):
        response = int(input(question))
    print("Correct!")
    return response
