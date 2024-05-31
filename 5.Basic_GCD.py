#GCD_recursion

'''
Pseudo Code : 

for (i=1 to m)
if(i%m & i%n)
{
    HCF = i 
}


'''


def GCD_recursion(a,b):
    if(b==0):
        return a
    else:
        return GCD_recursion(b,a%b) 

def GCD_loop(a,b):
    if a>b:
        small = b
    else:
        small = a
    
    for i in range(1,small+1):
        if((a%i == 0)) and (b%i == 0):
            gcd_value = i
    return (gcd_value)

def main():
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    print("GCD_recursion of",a,"and",b,"is",GCD_recursion(a,b))
    print("GCD_loop of",a,"and",b,"is",GCD_loop(a,b))
    

if __name__ == "__main__":
    main()
    