def factorial(x):
    product=1
    if x==0:
        return product
    else:
        for i in range(1,x):
            product=x*factorial(x-1)
        return product