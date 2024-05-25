#Prime Number is divide by itself
#if n/i==0

def prime_or_not(n):
    for i in range(2,n):
        if n%i==0: #divides by itself and Remainder is Zero
            print(n)
            print("Not a prime number")
            break
    else:
        print("Prime number")
    return i

def main():
    try:
        n=int(input("Enter a number: "))
        prime_or_not(n)
    except ValueError:
        print("Enter a valid number")


if __name__ == "__main__":
    main()