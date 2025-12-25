import plotly.express as px
import pandas as pd
#  مكتبة لرسم الرسوم البيانية التفاعلية في بايثون.
#يمكن تحريك الرسوم، التكبير،
#وعرض البيانات عند المرور على النقاط (hover).
#تعمل بسلاسة مع Pandas وNumPy.


# مثال بيانات
data = pd.DataFrame({
    "Age": [23, 25, 30, 22, 35, 40, 28],
    "Salary": [500, 600, 800, 400, 1000, 1200, 700],
    "Department": ["HR", "IT", "IT", "HR", "Finance", "Finance", "IT"]
})

# fig = px.scatter(data, x="Age", y="Salary", color="Department", size="Salary", hover_data=["Age"])
# fig.show()

# fig = px.bar(
#     data, 
#     x="Department", 
#     y="Salary", 
#     color="Department", 
#     barmode="group"       # عرض الأعمدة جنبًا إلى جنب
# )
# fig.show()

# fig = px.line(
#     data, 
#     x="Age", 
#     y="Salary", 
#     markers=True           # عرض العلامات على كل نقطة
# )
# fig.show()