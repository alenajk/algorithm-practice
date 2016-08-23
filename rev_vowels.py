def rev_vowels(str1):
    """Reverses the vowel order in a given string"""

    l1 = list(str1)
    vowels = ['a', 'e', 'i', 'o','u']
    vowel_order = []

    for char in l1:
        if char in vowels:
            vowel_order.append(char)

    new_vowel_order = vowel_order[::-1]

    for i in range(len(l1)):
        if l1[i] in vowels:
            l1[i] = new_vowel_order[0]
            new_vowel_order = new_vowel_order[1:]

    return ''.join(l1)
