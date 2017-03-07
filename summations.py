#adding all the digits in a number (assumed positive)

def digit_sum(n):
    total=0
    
    for i in range(n):
        num=n%10
        total+=num
        n=n/10
        
    return total