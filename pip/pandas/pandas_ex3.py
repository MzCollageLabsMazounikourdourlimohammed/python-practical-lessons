
#تستخدم لتعامل وادارة البيانات بشكل جدولي
import pandas as pd

#انشاء مثال تعامل مع بيانات 
data = {
    #إنشاء قاموس تعريفي بالشخصيات المقترحة 
    'Name': ['Mazouni', 'mohammed', 'abdelkader'],
    'Age': [22, 23, 25],
    'City': ['Algiers', 'Oran', 'Blida']
}
df = pd.DataFrame(data)

# print(df['Age'])         # الوصول لعمود
# print("\n")   
# print(df.iloc[1])        #  للصف الأول
# print("\n")   
# print(df.iloc[:1])      #  لأول صفين
# print("\n")   
print(df[df['Age'] >= 28])  #    'طباعة حسب شرط

    
print(df['Age'].max())