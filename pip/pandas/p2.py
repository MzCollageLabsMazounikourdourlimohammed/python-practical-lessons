#تستخدم لتعامل وادارة البيانات بشكل جدولي
import pandas as pd



#انشاء مصفوفة وتقديم لها قيم تعريفية 
# s= pd.Series([10, 20, 30, 40], index=['a','b','c','d'])
# print("Series:\n",s)

#====================
#انشاء مثال تعامل مع بيانات 
data = {
    #إنشاء قاموس تعريفي بالشخصيات المقترحة 
    'Name': ['Mazouni', 'mohammed', 'abdelkader'],
    'Age': [22, 23, 25],
    'City': ['Algiers', 'Oran', 'Blida']
}
df = pd.DataFrame(data)
#يقوم بانشاء جدول للبيانات المقترحة
# print("\nTable DataFrame:\n", df)
# print("\n")


# #=====
# print(df['Age'])         # الوصول لعمود
# print("\n")   
# print(df.iloc[1])        #  للصف الأول
# print("\n")   
# print(df.iloc[:1])      #  لأول صفين
# print("\n")   
print(df[df['Age'] >= 28])  #    'طباعة حسب شرط

    
print(df['Age'].max())

#===============

