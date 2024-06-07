# def fib1(n):
#     if n <=2: return 1
#     return fib1(n-1) + fib1(n-2)

# def fib2(n):
#     if n <=2: return 1
#     a, b = 1, 1
#     for i in range(n-2):
#         a, b = a+b, a
#     return a

# cache = {}
# def fib3(n):
#     if n in cache:
#         return cache[n]
#     if n <= 2:
#         result = 1
#     else:
#         result = fib3(n-1) + fib3(n-2)
#     cache[n] = result
#     return result

# def fib4(n):
#     if n<=2: return 1
#     fib_list = [1, 1]
#     while len(fib_list) < n:
#         fib_list.append(fib_list[-1] + fib_list[-2])
#     return fib_list[-1]


# import random

# class Dice():
#     def __init__(self, num_side, condition):
#         self.num_side = num_side
#         self.condition = condition

#     def roll(self):
#         score = random.randrange(self.num_side) + 1
#         if not self.condition(score):
#             raise 1
#         return score
    
# even_dice = Dice(6, lambda x : x % 2 == 0)
# try:
#     total_score = 0
#     for _ in range(3):
#         total_score += even_dice.roll()
#     print('Win!')
# except:
#     print('Lose!')
# finally:
#     print('Total:', total_score)



# x = [1 ,2 ,3]
# y = [x] * 3
# print(y)

# y[0][1] = 4
# print(y)
# print(sum(y[0])+sum(y[2]))


# x =[a, b, c]
# y = [x] * 3
# y[0][1] = d
# print(sum(y[0]) + sum(y[2]))


# a = []
# a = [a[-1]]
# print(a)



# [[ '1' ,'John, Mr. Henry' · 'A2'],
# [ '2' ,'Allen, Mr. Marti' 'C4'],
# [ ' 3' , 'Patrick' , 'B2 ' ],
# [ '4', 'Graham, Ms. Catherine' 'C17' ],
# [ '5', 'Peter, Mrs. Emile', 'A1'],
# [ '6' '', 'B3 '],
# ['7' , 'John, Mr. Kim' , 'A' ],
# ['8' ,  'Wang, Mrs. Olivia' . 'B' ],
# ['9', 'Mr', ''],
# ['10', '', '23']]

# def func1(): 
#     female = 0
#     for line in passenger_list:
#         if ("Mrs." in line[1] or "Ms. " in line[1]):
#             female += 1
#         print("female: %d" % female) 

# def func2() :
#     a_class = 0 
#     b_class = 0 
#     c_class = 0 
#     for line in passenger_list: 
#         if ("A" in line[2]): 
#             a_class += 1 
#         elif ("B" in line[2]): 
#             b_class += 1 
#         else: 
#             c_class += 1 
#     print ( "A Class: %d" % a_class) 
#     print("B Class: %d" % b_class) 
#     print ("C Class: %d" % c_class) 
# def func3(): 
#     import re 
#     male = 0 
#     mr = re.compile(r'.*Mr.*') 
#     for line in passenger_list: 
#         if(mr.search(line[1])):
#             male += 1 
#             print ("male: %d" % male) 
# def func4(): 
#     for line in passenger_list: 
#         line[2] = ''.join(i for i in line[2] if not i.isdigit())
# def func5(): 
#     for line in passenger_list: 
#         line[1] = ''.join(line[1].split(", ")[1:])


# class Beverage:
#     def __init__(self, size, name):
#         self.name = name
#         self.caffeine = 0
#         self.size = size

#     def __repr__(self):
#         return f"{self.name} drink"
    
#     def contains_caffeine(self):
#         if (self.caffeine):
#             return f"Contains {self.caffeine}mg per cup"
# class Coffee(Beverage):
#     def __init__(self, size = "Small", name ="Coffee"):
#         super().__init__(size, name)
#         self.caffeine = 125

#     def price(self):
#         return 5000
    
# class Milk(Beverage):
#     def __init__(self, size = "Small", name = "Milk"):
#         super().__init__(size, name)
#         self.flavor = "Creamy"
#         self.caffeine = 0

#     def price(self):
#         return 3000
    
# class CafeLatte(Coffee, Milk):
#     def __init__(self, size):
#         super().__init__(size, "CafeLatte")
"""
image: list[list[int]]. N X M image (N, M > 0, N and M can be different)
result: list[int]

Example:
funX([[1,2], [3,4]]) -> [1, 2, 3, 4]
"""

def fun1(image):
    row = len(image)
    col = len(image[0])

    result = [0] * (row * col)
    for r in range(row):
        for c in range(col):
            result[r*col + c] = image[r][c]
    return result

def fun2(image):
    row = len(image)
    col = len(image[0])

    result = [0] * (row * col)
    for i in range(row * col):
        r = i // row
        c = i % row
        result[i] = image[r][c]
    return result

def fun3(image):
    result = []
    for row in image:
        result.append(row)
    return result

def fun4(image):
    result = []
    for row in image:
        for pixel in row:
            result.append(pixel)
    return result


def fun5(image):
    row = len(image)
    col = len(image[0])

    result = []
    for c in image(col):
        for r in range(row):
            pixel = image[r][c]
            result.append(pixel)
    return result


#Class for 2x2 matrix
# |a b|
# |c d|

class TwoByTwoMatrix():
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def (A)(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        d = self.d + other.d
        return TwoByTwoMatrix(a, b, c, d)
    
    def __mul__(self,other):
        a = self.a * other.a + self.b * other.c
        b = self.a * other.b + self.b * other.d
        c = (B)
        a = self.c * other.b + self.d * other.d

    def __repr__(self):
        return "|{} {} |\n| {} {}|".(C)(self.a, self.b, self.c, self.d)

mat_a = TwoByTwoMatrix(1,1,1,1)
mat_b = TwoByTwoMatrix(2,4,5,6)