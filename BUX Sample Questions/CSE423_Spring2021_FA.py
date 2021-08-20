import random

# DDA
# Imagine  P1 ( x1 ,  y1 ) = (-30, 93) and  P2 ( x2 ,  y2 ) = (-84, -137) are two points of the same line.
# If we apply the DDA algorithm from  P1  then how will x and y change?
x1 = random.randint(-40, 40)
y1 = random.randint(50, 100)
x2 = random.randint(-100, -80)
y2 = random.randint(-150, -100)

m = (y2-y1) / (x2-x1)
floating_m = round(1/m, 2)
x_ans = round(1/m)

# Cyrus-Beck
# The parametric equation of a line is  P(t)=P0+(P1−P0)t.
# If  P0(x0,y0)  = (-30, 93) and  P1(x1,y1)  = (-84, -137),
# then what should be the coordinates of the midpoint between  P1  and  P(0.819) ?
x0 = random.randint(-40, 40)
y0 = random.randint(50, 100)
x1 = random.randint(-100, -80)
y1 = random.randint(-150, -100)

t = 0.819
x_t = x0 + t * (x1 - x0)
y_t = y0 + t * (y1 - y0)
x_ans = round((x1 + x_t)/2, 2)
y_ans = round((y1 + y_t)/2, 2)


# Transformation
# Suppose, a composite transformation is defined as scaling 5 times in X-axis and 6 times in Y-axis
# with respect to point (5, 6). Calculate the composite transformation matrix in homogenous form.
# Then, find the new coordinates of the point (17, 27) after transformation.
def matrix_multiplication(a, b):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    # iterating by row of A
    for i in range(len(a)):

        # iterating by column by B
        for j in range(len(b[0])):

            # iterating by rows of B
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    for r in result:
        print(r)
    print('--------')
    return result


x = random.randint(2, 10)
y = random.randint(2, 10)
scale_x = random.randint(2, 10)
scale_y = random.randint(2, 10)
p_x = random.randint(2, 40)
p_y = random.randint(2, 40)
print(x)
print(y)
print(scale_x)
print(scale_y)
print(p_x)
print(p_y)
t = [
    [1, 0, x],
    [0, 1, y],
    [0, 0, 1]
]
s = [
    [scale_x, 0, 0],
    [0, scale_y, 0],
    [0, 0, 1]
]
t_inverse = [
    [1, 0, -x],
    [0, 1, -y],
    [0, 0, 1]
]
p = [
    [p_x],
    [p_y],
    [1]
]
ans = matrix_multiplication(matrix_multiplication(matrix_multiplication(t, s), t_inverse), p)
ans_x = ans[0][0]
ans_y = ans[1][0]
print(ans_x)
print(ans_y)
