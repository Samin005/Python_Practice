a = int(input())
b = int(input())
c = a + b
print(c)

hours_worked = int(input())
if hours_worked > 40:
    print("Overtime pay")
else:
    print("Regular pay")

print(10 / 3)
print(10 // 3)
print(10 ** 3)
print(round(2.4))
print(abs(-5.2))

num = 10 + 2 * 2 ** 3 % 2  # priority: **, %, * or /, + or -
print(num)

num1 = 4
num2 = 4
print(num1 is num2)
# print(num1 is 4)  # Error

num = 10
num -= 30
print(num)

# num = input()
# num = int(num[len(num) - 1])
# print(num)

num = 7
print(-(-num // 2))  # 7 // 2 = 3 but -(-7 // 2) = 4, gives you the ceiling of the floating point number

# while loops
print('--- while Loop ---')
i = 0
j = 1
a = 'a'
while i < 8:
    j *= 2
    print(j)
    a *= 2
    i += 1
print(a)
