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
#يقوم بانشاء جدول للبيانات المقترحة
print("\nTable DataFrame:\n", df)
print("\n")