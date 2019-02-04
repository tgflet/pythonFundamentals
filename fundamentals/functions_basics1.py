#1
# def a():
#     return 5
# print(a())
# predict: 5
# Correct prediction

#2
# def a():
#     return 5
# print(a()+a())
# predict: 10
# Correct predicition

#3
# def a():
#     return 5
#     return 10
# print(a())
# predict: 5
# correct prediction

#4
def a():
    return 5
    print(10)
print(a())
# predict: 5
# correct prediction

#5
def a():
    print(5)
x = a()
print(x)
# predict: 5
# wrong: forgot to predict none as a second result

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2)+a(2,3))

# predict: 8
# wrong: error results because '+' is not supported by null types. to get a result change "print(b+c)" to "return(b+c"

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# predict: 7
# wrong: since the numbers are converted to strings they no longer function mathematically, they result in the string 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# predict: 100, 10
# correct, thr function exits before return 7 is ever factored

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# predict: 7,14,21
# correct

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# predict: 8
# correct

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# predict: 500,500,300,500
# correct

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# predict: 500,500,300,500
# correct

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# predict: 500,500,300,300
# correct

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# predict: 1,3,2
# correct

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# predict: 1,3,5,10
# correct