def factoril(n):
    if n==0:
        return 1
    else:
        fact =factoril(n-1)*n
        return fact
print(factoril(4))