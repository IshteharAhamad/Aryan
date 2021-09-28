def run(n):
    if n==0:
        return
    
    print(n)
    
    run(n-1)
    print()
    print(n)
    
n = 3
run(n)
#output 3 2 1
print("************ both are defferent to eachothers ************")
def runn(m):
    if m==0:
        return
    runn(m-1)
    print(m)
m =int(input("enter number : "))
runn(m)