#print diya output dakha jai
'''triple cotetion diya comment kora jai'''
def calculator(x,y,action):
    if action == "Multiply":
        return x * y
    elif action == "divide":
        return x / y
    elif action == "minus":
        return x - y
    else:
        return x + y
    
print(calculator(6,15,"Multiply"))