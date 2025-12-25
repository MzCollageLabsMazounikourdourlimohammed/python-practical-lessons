c = [1, 2, 3, 4, 5]

print(c[1:5])   # [2, 3, 4] 
print(c[0:2])   # [1, 2 ,3]

print(c[:3])    # [1, 2, 3]
print(c[:2])    # [1 ,2]
print(c[2:])    # [3, 4, 5]
print(c[0:])    # [1 ,2 ,3 ,4 ,5]
print(c[::4])   # [3, 4, 5]

# # ===========
print(sum(c))     # 15
print(max(c))     # 5
print(min(c))     #1
