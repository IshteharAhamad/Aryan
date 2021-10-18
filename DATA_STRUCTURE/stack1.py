stack=[]
def push():
    element = int(input("Enter the Element in stack : "))
    stack.append(element)
    print(stack)
def pop_Element():
    if len(stack)==0:
        print("Stack is unedrflow condition..")
    else:
        rm=stack.pop()
        print("Removed element : ",rm)
        print(stack)
while True:
    print("Select the option \n1-> push \n2-> pop \n3-> Exit ")
    choice = int(input("choose the option : "))
    if choice==1:
        push()
    elif choice==2:
        pop_Element()
    elif choice==3:
        break
    else:
        if choice>3 or choice==0:
            for choice in range(3):
                print("wrong choice .....")
                print("Please Enter the right choice .....")
                if choice==3:
                
                    break
        
