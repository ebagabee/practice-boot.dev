def join_strings(strings):
    result = ""

    for i in range(1, len(strings)):
        if i == 1:
            result = strings[0]
        result = result + "," + strings[i]

    return result
