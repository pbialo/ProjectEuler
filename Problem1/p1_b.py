'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Problem 1 using sum of series

def main():
    s = (sumOfMultiples(3, 999) + sumOfMultiples(5, 999) - sumOfMultiples (15, 999))
    print (s) 
    
def sumOfMultiples(n, p):
    return n*(p//n)*((p//n)+1)/2
    
if __name__ == "__main__": main()
