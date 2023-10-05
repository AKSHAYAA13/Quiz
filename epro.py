import random
oper=['+','-','*']
min=1
max=12
count = 0
def test():
    global right
    right=random.randint(min,max)
    global a
    a=random.choice(oper)
    global left
    left=random.randint(min,max)
    exp=str(right)+a+str(left)+"="
    b=input(exp)
    return(eval(b))
def checklist():
        if(a=='+'):
            result=right+left
        elif(a=='-'):
            result=right-left
        else:
            result=right*left
        return(result)
for i in range(1,11):
    print("question",i)
    userinput=test()
    c=checklist()
    if c == userinput:
        print("Your answer is correct")
        count+=1
    else:
        print("Your answer is incorrect")
print("You have successfully completed the maths quiz")
print("Your score is",count,"out of 10")
if count<=7:
    print("sorry you lose the game")
elif count==10:
    print("awesome")
else:
    print("Your won the game")

