def zero(num = 0): #your code here
    if num != 0:
        num2 = 0
        num = operate(num, num2)
    return num
def one(num = 1): #your code here
    if num != 1:
        num2 = 1
        num = operate(num, num2)
    return num
def two(num = 2): #your code here
    if num != 2:
        num2 = 2
        num = operate(num, num2)
    return num
def three(num = 3): #your code here
    if num != 3:
        num2 = 3
        num = operate(num, num2)
    return num
def four(num = 4): #your code here
    if num != 4:
        num2 = 4
        num = operate(num, num2)
    return num
def five(num = 5): #your code here
    if num != 5:
        num2 = 5
        num = operate(num, num2)
    return num
def six(num = 6): #your code here
    if num != 6:
        num2 = 6
        num = operate(num, num2)
    return num
def seven(num = 7): #your code here
    if num != 7:
        num2 = 7
        num = operate(num, num2)
    return num
def eight(num = 8): #your code here
    if num != 8:
        num2 = 8
        num = operate(num, num2)
    return num
def nine(num = 9): #your code here
    if num != 9:
        num2 = 9
        num = operate(num, num2)
    return num

def plus(num): 
    return ["+", num]
def minus(num): 
    return ["-", num]
def times(num): 
    return ["*", num]
def divided_by(num): 
    return ["/", num]

def operate(num1, num2):
    if num1[0] == "+":
        return num1[1] + num2
    if num1[0] == "-":
        return num2 - num1[1] 
    if num1[0] == "*":
        return num1[1] * num2
    if num1[0] == "/":
        return num2 // num1[1]  

print (eight(minus(three())))