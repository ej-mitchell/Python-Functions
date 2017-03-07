def calculate_years(principal, interest, tax, desired):
    #raise NotImplementedError("TODO: calculate_years")
    Y=0
    if principal==desired:
        return 0
    while principal<desired:
        Y+=1
        principal+=principal*interest*(1-tax)
        if principal>=desired:
            return Y