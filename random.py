num = int(input("Enter the first number : "))
number = int(input("Enter the second number : "))
def calculation(num,number):
    product  = num * number
    if product>1000:
        #print ("Sum of two numbers : ",num +number)
        return (num+number)
    else:
        #print ("product : ",num*number)
        return(num*number)
result = calculation(num,number)
print("Result : ",result)