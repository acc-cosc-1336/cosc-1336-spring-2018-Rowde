#write the import for the function get_count_A_C_G_and_T_in_string from assignment 6 file
from assignment6 import get_count_A_C_G_and_T_in_string
'''
Using function get_count_A_C_G_and_T_in_string create a main function and...
Call the function get_count_A_C_G_and_T_in_string from assignment 6 file
With the string AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC as an argument
Sample Output:

DNA String:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
A 20, C 12, G 17, T 21


Call the main function in Python Shell or in this file.
'''
def main():
    dna_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

    num_A, num_C, num_G, num_T = get_count_A_C_G_and_T_in_string(dna_string)

    print('DNA string:')
    print(dna_string)
    print('A ',num_A,'C ',num_C,'G ',num_G,'T ',num_T)

main()
    
