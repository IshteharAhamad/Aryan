lst1 = [1,2,3,4,5,6,7,9,8,9,8,7,6,5,4,4,3,3,2,2,1]
ls =[]
for item in lst1:
    if item not in ls:
        
        ls.append(item)
print(ls)