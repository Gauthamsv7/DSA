def factorial (n):
    factorial = 1
    for i in range(n):
        factorial*=i+1 #Factorial Iterates to i
        
    return factorial



def main():
    try:
        n = int(input("Enter a number: "))
        print(factorial(n))
    except ValueError:
        print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    main()