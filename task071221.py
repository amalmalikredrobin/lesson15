# def sum(a, b):
#     return a +b 

# print(sum(6, 5))

# def calcSquares(list):
#     newList = []
#     for num in list:
#         newList.append(num * num)
#     return newList

# print(calcSquares([1, 2, 3, 4, 5]))

# calcSquares = lambda list: [num * num for in list]

# print(calcSquares([1, 2, 3, 4, 5]))

# sum = lambda num1: lambda num2: num1 + num2

# print(sum((2)(3)))


# def upper(txt):
#     return txt.upper()

# def lower(txt):
#     return txt.lower()

# def say_hello(func):
#     greeting = func('Hello I am Amalmalik')
#     print(greeting)


# say_hello(upper)
# say_hello(lower)

# print(upper('Hello'))
# print(lower('PHP'))

# string = 'Hello I am Amalmalik'
# urlFriendly = []

# for char in string:
#     if char == ' ':
#         urlFriendly.append('_')
#     else: urlFriendly.append(char)

# urlFriendly = ''.join(urlFriendly)
# print(urlFriendly)

# string2 = 'Hello I am Amalmalik'
# urlFriendly2 = string2.replace(' ', '_')
# print(urlFriendly2)

def calcLoan(credit, period, interest):
    total = credit + credit * (interest / 100) * period
    per_month = total / (period * 12)
    per_month_sums = per_month * 10800
    return f'You have to pay {int(per_month_sums)}sums per month'

calcLoan(1000, 3, 26) #You to payh 534000 sums per month