#this function returns true if the given string
#is an integer number, and false, otherwise
def is_int(line):
    is_num = True
    try:
        int(line)
    except ValueError:
        is_num = False
    return is_num


#computing the gcd of two numbers
#this function returns a string as an answer
def gcd(a, b):
    if(not is_int(a)) or (not is_int(b)):
        return 'mistake'
    else:
        a=abs(int(a))
        b=abs(int(b))
        if a == 0:
            return str(b)
        if b == 0:
            return str(a)
        if a > b:
            small = b
        else:
            small = a
        for i in range(1, small + 1):
            if((a % i == 0) and (b % i == 0)):
                gcd = i

        return str(gcd) 


#this function receives a string line as a parameter,
#splittes it into two parts, and returns that two parts
def get_nums(line):
    temp = line.split()
    return (str(temp[0]), str(temp[1]))

