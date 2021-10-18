display = lambda x:print(x)
display("hello mamamamam")
print("****************************** map ************************************")
liist =[5,10,15,20,25,30]
ls  =[]
def square(liist):
    for item in liist:
        ls.append(item**2)
    return ls
print(square(liist))