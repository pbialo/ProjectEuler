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
                print (n)
                L.append(n)
            b += 1
        a += 1
    m = max(L)
    print (m)

if __name__ == "__main__": main()
