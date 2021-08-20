import random

x0 = random.randint(1, 45)
y0 = random.randint(50, 100)
x1 = random.randint(50, 100)
y1 = random.randint(1, 45)

m = abs((y1-y0)/(x1-x0))

if -1 < m < 1:
    ans_x1 = x0 + 1
    ans_x2 = ans_x1 + 1
    ans_x3 = ans_x2 + 1
    ans_x4 = ans_x3 + 1
    ans_x5 = ans_x4 + 1
    ans_x6 = ans_x5 + 1
    ans_y1 = round(y0 - m)
    ans_y2 = round(y0 - 2*m)
    ans_y3 = round(y0 - 3*m)
    ans_y4 = round(y0 - 4*m)
    ans_y5 = round(y0 - 5*m)
    ans_y6 = round(y0 - 6*m)
else:
    ans_x1 = round(x0 + 1/m)
    ans_x2 = round(x0 + 2/m)
    ans_x3 = round(x0 + 3/m)
    ans_x4 = round(x0 + 4/m)
    ans_x5 = round(x0 + 5/m)
    ans_x6 = round(x0 + 6/m)
    ans_y1 = y0 - 1
    ans_y2 = ans_y1 - 1
    ans_y3 = ans_y2 - 1
    ans_y4 = ans_y3 - 1
    ans_y5 = ans_y4 - 1
    ans_y6 = ans_y5 - 1

print((x0, y0))
print((x1, y1))
print(m)
print(ans_x1, ans_y1)
print(ans_x2, ans_y2)
print(ans_x3, ans_y3)
print(ans_x4, ans_y4)
print(ans_x5, ans_y5)
print(ans_x6, ans_y6)
