import numpy as np
def GDA(start,gradient,lrate,iteration,tolerance=0.01):
    steps=[start]
    x=start
    for i in range(iteration):
        diff=lrate*gradient(x)
        if np.abs(diff)<tolerance:
            break
        x-=diff
        steps.append(x)
    return steps,x,len(steps),lrate

def gradient_fun(x):
    return (x+3)*(x+3)

history,result,y,lr=GDA(2,gradient_fun, 0.1,100)
print("steps in GDA: " ,history)
print("learing rate: ", lr)
print("local minima: ", result)
print("No. of steps required to reached local minima: ",y)