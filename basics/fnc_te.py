# #انشاء دالة اولية
def Welcome():
    print("Hello!")
Welcome()
Welcome()
Welcome()
 

# #  # انشاء دالة مع خصائص 

def hello(name):
    print("Hello", name)
hello("MZ")

# # دالة بمتغيرين
def add(a, b):
    print(a + b)
add(3,2)
add(34,4)

# #=========
# #قمية مرجعة 
# def add1(a, b):
#     return a + b

# r=add1(5,10)
# print(r)

# #==========


# def Users(name="Enter Name"):
#     print("Hello",name)
# Users()
# Users("Mazzouni")

# #=======
# #يمكن للدالة ارجاع اكثر من قيمة 
# def calc(a, b):
#     return a+b, a-b, a*b

# sum2, diff, mul = calc(10, 5)
# print(sum2,diff,mul)

# #==========
# #يمكن للدالة تقبل عدد غير معرف من قيم 
# def total(*Num):
#     print(sum(Num))

# total(1,2,4,3,5,7,8,9,10)

# #==========
# #نستخدم دالة داخل دالة 

def One():
    def Two():
        print("Second Function")
    Two()
One()

# #=========
# #مثال عن استخدام الدوال مع المصفوفات

def arr_sum(arr):
    total = 1
    for x in arr:
        total -= x
    return total

print(arr_sum([10, 20, 30,40]))