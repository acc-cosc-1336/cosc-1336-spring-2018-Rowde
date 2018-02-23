def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''
    A_count=0
    C_count=0
    G_count=0
    T_count=0

    for ch in dna_string.upper():
        if ch == 'A':
            A_count += 1

    for ch in dna_string.upper():
        if ch == 'C':
            C_count += 1

    for ch in dna_string.upper():
        if ch == 'G':
            G_count += 1

    for ch in dna_string.upper():
        if ch == 'T':
            T_count += 1

    return A_count, C_count, G_count, T_count
    
