str = input("enter string : ")
for i in range(0,len(str),2):
    print("index [",i,"] -> ",str[i])
print("******************** Using function ******************")
str1 =input("enter the string : ")
def slice(str1):
    for i in range(0,len(str1),2):
        print("index[",i,"] ->",str1[i])


slice(str1)