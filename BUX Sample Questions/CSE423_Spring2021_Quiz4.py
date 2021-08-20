import random

#viewing frame
global xmin, ymin, xmax, ymax
xmin = random.randint(-300, -100)
xmax = random.randint(200, 300)
ymin = random.randint(-180, -20)
ymax = random.randint(100, 220)

# xmin = -279
# xmax = 270
# ymin = -76
# ymax = 213

# line to clip
global Ax, Ay, Bx, By, Bx1, By1, m
Ax = random.randint(xmin, xmax)
Ay = random.randint(ymin, ymax)

if(random.random()>0.5):
    Bx1 = xmin - random.randint(10, 100)
else:
    Bx1 = xmax + random.randint(10, 100)
if(random.random()>0.5):
    By1 = ymin - random.randint(10, 100)
else:
    By1 = ymax + random.randint(10, 100)

Bx, By = Bx1, By1

# Ax = -130
# Ay = -2
# Bx = -348
# By = 285
m = (By-Ay)/(Bx-Ax)

def CompOutCode(x, y):
    code=['0','0','0','0']
    #top
    if(y>ymax):
        code[0] = '1'
    #bottom
    elif (ymin>y):
        code[1] = '1'
    #right
    if(x>xmax):
        code[2]= '1'
    #left
    elif(xmin>x):
        code[3]= '1'
    return ''.join(code)

global outcodeA, outcodeB, Bs, Bcodes
outcodeA= CompOutCode(Ax, Ay)
outcodeB= CompOutCode(Bx, By)
Bs = [0]*4
Bcodes=[0]*2
Bcodes[0] = outcodeB
Bcode0 = Bcodes[0]

def InterSecting(id):
    global Ax, Ay, Bx, By, outcodeA, outcodeB, Bs
    outcodeOut = 'xxxx'
    if outcodeA!='0000':
        outcodeOut = outcodeA
    elif outcodeB!='0000':
        outcodeOut = outcodeB
    x, y=0,0
    if outcodeOut[0]=='1':
        x= Bx + (1/m)*(ymax-By)
        y = ymax
    elif outcodeOut[1]=='1':
        x= Bx + (1/m)*(ymin-By)
        y=ymin
    elif outcodeOut[2]=='1':
        y =  By+m*(xmax-Bx)
        x=xmax
    elif outcodeOut[3]=='1':
        y = By+m*(xmin-Bx)
        x=xmin
    if (outcodeOut==outcodeA):
        Ax, Ay =round(x),round(y)
        outcodeA = CompOutCode(Ax, Ay)
    else:
        Bx, By=round(x),round(y)
        outcodeB = CompOutCode(Bx, By)
    Bs[id], Bs[id+1] = round(x),round(y)

def checkOutCode(expect, ans):
    id=int(expect)
    check1, check2 = False, False
    msg1, msg2= "Wrong answer", "Wrong answer"
    try:
        if(ans[0]==outcodeA):
            check1, msg1= True, "Correct answer"
    except:
        msg1="Invalid input"
    try:
        if(ans[1]==Bcodes[id]):
            check2, msg2= True, "Correct answer"
    except:
        msg2="Invalid input"
    return {'overall_message': 'Checked','input_list': [{ 'ok': check1, 'msg': msg1},{ 'ok': check2, 'msg': msg2}] }

InterSecting(0)
B0, B1 = int(Bs[0]), int(Bs[1])
Bcodes[1] = outcodeB
Bcode1=Bcodes[1]

if(Bcode1=='0000'):
    Bs[2], Bs[3] = Bs[0], Bs[1]
    B2, B3 = int(Bs[0]), int(Bs[1])
else:
    InterSecting(2)
    B2, B3 = int(Bs[2]), int(Bs[3])

def checkInterSecting(expect, ans):
    id=int(expect)
    check1, check2 = False, False
    msg1, msg2= "Wrong answer", "Wrong answer"

    try:
        if(int(ans[0])==int(Bs[id])):
            check1, msg1= True, "Correct answer"
    except:
        msg1="Invalid input"
    try:
        if(int(ans[1])==int(Bs[id+1])):
            check2, msg2= True, "Correct answer"
    except:
        msg2="Invalid input"
    return {'overall_message': 'Checked','input_list': [{ 'ok': check1, 'msg': msg1},{ 'ok': check2, 'msg': msg2}] }
