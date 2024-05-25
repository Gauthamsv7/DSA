#1,1,2,3,5,8......


def fibnocci_series(n):
    a = 0
    b = 1
    for i in range(n): #A = B, B=C and operations over them
        c = a+b
        a = b
        b = c
        print(c)
        #return c


def main():
    try:
        n = int(input("Enter the number : "))
        fibnocci_series(n)
    except ValueError:
        print("Enter a valid number")

if __name__ == "__main__":
    main()