#Recursive Func : A Function calling itself

def recursive_fatorial(n):
    if n == 0:
        return 1
    
    return n * recursive_fatorial(n-1) #Func Calls itself

def main():
    try:
        n = int(input("Please Enter the Number : "))
        print("Finale Value : ",recursive_fatorial(n))
        print("All Values : \n")
        for i in range(1,n+1):
            print(i,recursive_fatorial(i))
    except ValueError:
        print("Please Enter a Valid Number")
        
if __name__ == "__main__":
    main()
    