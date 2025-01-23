def my_function(x):
    if x == 0:
        return 0
    elif x < 0:
        return 0 #Handle negative inputs
    else:
        result = 0
        for i in range(1, x + 1):
            result += i
        return result