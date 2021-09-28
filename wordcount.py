str = input("Enter the sentence : ")
word = input("count word : ")
def counts(str,word):
    count = 0
    ls=str.split()
    for i in ls:
        if i == word:
            count +=1
        print(i)
    return count
print(counts(str,word))