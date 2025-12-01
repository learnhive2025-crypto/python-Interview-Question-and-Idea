##DataFrame → 2-dimensional table (rows & columns)
import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Krishna"],
    "Age": [25, 22, 30],
    "City": ["Delhi", "Mumbai", "Chennai"]
}

df = pd.DataFrame(data)
print(df)
