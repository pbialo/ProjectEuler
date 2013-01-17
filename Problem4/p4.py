'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def main():
    a = 100
    L = []
    while a < 1000:
        b = 100
        while b < 1000:
            n = a*b
            stringForward = str(n)
            stringBackward = stringForward[::-1]
            if stringForward == stringBackward:
                L.append(n)
            b += 1
        a += 1
    print (max(L))

if __name__ == "__main__": main()
