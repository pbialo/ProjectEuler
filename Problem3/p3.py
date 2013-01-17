'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def main():
    factors = []
    a = 2 #The first factor we will be using
    n = 600851475143
    while (n > 1):
        while (n % a == 0):
            factors.append(a)
            n = n/a
        a = a + 1
        if ((a * a) > n):
            if (n > 1):
                factors.append(n);
                break;
    print (factors[-1])
if __name__ == "__main__": main()
