list=list(input("enter list:")) #[12,3,44,444,66,87,23]
def check(list):
    first =list[0]
    last =list[-1]
    if first==last:
        return True
    else:
        return False

print(check(list))