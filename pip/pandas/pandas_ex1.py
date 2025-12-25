#تستخدم لتعامل وادارة البيانات بشكل جدولي
import pandas as pd

# انشاء مصفوفة وتقديم لها قيم تعريفية 
s= pd.Series([10, 20, 30, 40], index=['a','b','c','d'])
print("Series:\n",s)
