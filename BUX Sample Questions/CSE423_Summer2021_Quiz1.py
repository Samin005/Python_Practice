import random

x0 = random.randint(-100, -1)
y0 = random.randint(-100, -1)
x1 = random.randint(1, 100)
y1 = random.randint(1, 100)

m = (y1-y0)/(x1-x0)

if -1 < m < 1:
    ans_x1 = x0 + 1
    ans_x2 = ans_x1 + 1
    ans_x3 = ans_x2 + 1
    ans_x4 = ans_x3 + 1
    ans_y1 = round(y0 + m)
    ans_y2 = round(y0 + 2*m)
    ans_y3 = round(y0 + 3*m)
    ans_y4 = round(y0 + 4*m)
else:
    ans_x1 = round(x0 + 1/m)
    ans_x2 = round(x0 + 2/m)
    ans_x3 = round(x0 + 3/m)
    ans_x4 = round(x0 + 4/m)
    ans_y1 = y0 + 1
    ans_y2 = ans_y1 + 1
    ans_y3 = ans_y2 + 1
    ans_y4 = ans_y3 + 1

print(ans_x1, ans_y1)
print(ans_x2, ans_y2)
print(ans_x3, ans_y3)
print(ans_x4, ans_y4)
