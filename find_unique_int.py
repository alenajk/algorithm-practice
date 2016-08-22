def find_unique_int(my_list):
    """Returns the unique integer in a list of integers
    given that there is only one unique integer"""

    s = set()
    for item in my_list:
        if item in s:
            s.remove(item)
        else:
            s.add(item)
    return s.pop()