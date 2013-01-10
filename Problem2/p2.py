'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def main():
    s = 0
    a = 1 #The current term (F1)
    b = 1 #The previous term (F0)
  
    c = 0 #Temp value
 
    while a < 4000000:
        if a % 2 == 0:
            s = s + a
        c = a
        a = c + b
        b = c
        
    print (s)
if __name__ == "__main__": main()