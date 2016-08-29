def generate_products(l):
    """Generates a new list with product of all ints
    in list except for the int at given index
    [2,1,1,4] --> [4,8,8,2]"""

    if not l:
        return l

    if len(l) == 1:
        return 1

    if 0 in l:
        return generate_products_if_zeros(l)

    # Initialize a total product variable
    total_product = 1

    for i in range(len(l)):
        total_product *= l[i]

    prod_list = []
    for i in range(len(l)):
        val = total_product/l[i]
        prod_list.append(val)

    return prod_list

def generate_products_if_zeros(l):
    """Returns desired output list if input list has
    any zeros in it"""

    # If more than one 0 in list, return
    # list of same length with all 0s
    if l.count(0) > 1:
        return [0]*(len(l))
    
    # If there is only one 0 in the list
    else:
        
        prod_list = []
        zero_location = l.index(0)
        total_prod_excl_zero = 1
        
        # Compute total product excluding the 0
        for i in range(len(l)):
            if i != zero_location:
                total_prod_excl_zero *= l[i]

        # Place 0s and total product exluding 0 into new list
        for i in range(len(l)):
            if i == zero_location:
                prod_list.append(total_prod_excl_zero)
            else:
                prod_list.append(0)

    return prod_list

##################### Alternative method #####################

def generate_prods2(l):
    """Generates a new list with product of all ints
    in list except for the int at given index
    [2,1,1,4] --> [4,8,8,2]"""

    if not l:
        return l

    if len(l) == 1:
        return 1

    cumulative_prod_list = []
    prod = 1
    
    # Generate cumulative product list from input list
    for i in range(len(l)):
        cumulative_prod_list.append(prod)
        prod *= l[i]

    prod_list = []

    # Compute products and add to prod_list
    multiplier = 1
    for i in range(len(l)-1,-1,-1):
        val = l[i]
        prod_list.append(cumulative_prod_list[i]*multiplier)
        multiplier *= val

    return prod_list[::-1]

