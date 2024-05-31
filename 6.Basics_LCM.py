def lcm(a,b):
    max_num = max(a,b)
    while True:
        if (max_num % a == 0) and (max_num % b ==0):
            return max_num
            break
        max_num += 1
def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The LCM of",a,"and",b,"is",lcm(a,b))
    
if __name__ == "__main__":
    main()