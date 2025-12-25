# #يمكن للدالة ارجاع اكثر من قيمة 

def calc(a, b):
    return a+b, a-b, a*b

sum2, diff, mul = calc(10, 5)
print(sum2,diff,mul)