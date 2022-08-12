import sys
from gcd_functions import *

#this function performs the testing
def main():
    i_file = open("input.txt", 'r')
    o_file = open("output.txt", 'w')
    input_list = i_file.read().splitlines()
    for line in input_list:
        a, b = get_nums(line)
        o_file.writelines(gcd(a, b) + '\n')
    i_file.close()
    o_file.close()
main()
