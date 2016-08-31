def get_min_leftover_item(money, options):
    """You go into a grocery store with a fixed amount of money, wanting to spend
    as much of it as possible on a single item. This function returns the item
    that will allow you to accomplish this, and how many of it you can afford.

    >>> get_min_leftover_item(20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})
    ('avocados', 20)

    """
    
    leftover = money
    item = ''

    for option, cost in options.items():
        potential_leftover = get_min_leftover(money, cost)
        if potential_leftover < leftover:
            leftover = potential_leftover
            item = option

    return item, int(money/options[item])

def get_min_leftover(money, cost):
    """Returns minimum leftover possible for given cost and amount of money"""

    return round(money%cost, 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()