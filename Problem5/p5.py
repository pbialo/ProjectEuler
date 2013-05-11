'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def main():

    a = 1
    while (a < 300000000):
        div = True
        for x in reversed(range(10, 20)):
            if (a % x != 0):
                div = False
                break
        if (div == True):
            print (a)
            break
        a += 1


if __name__ == "__main__": main()
