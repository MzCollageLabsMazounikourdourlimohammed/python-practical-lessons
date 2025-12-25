import pandas as pd

data = {
    "Name": ["Fares", "MZ", "Sarah"],
    "Score": [80, 90, 70]
}

df = pd.DataFrame(data)
print(df)
print(df["Score"].mean())
