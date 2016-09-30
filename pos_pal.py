# Determine whether a string can be rearranged into a palindrome

def pal_pos(s):

    if not s:
        return False

    chars = set()
    for char in s:
        if char in chars:
            chars.remove(char)
        else:
            chars.add(char)

    # If len is even, want chars set to be empty
    if len(s)%2 == 0:
        if not chars:
            return True
        return False

    # If len is odd, want chars set to have exactly 1 item
    elif len(s)%2 != 0:
        if len(chars) == 1:
            return True
        return False
