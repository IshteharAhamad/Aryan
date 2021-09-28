def recursion(count):
    if count==10: # base case condition to stop recursion function
        return 0
    else:
        print("hello world",count)
        recursion(count+1)
count = 0
recursion(count)