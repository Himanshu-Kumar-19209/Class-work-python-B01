import pandas as pd

# Create a simple series
s = pd.Series([10, 20, 30, 40])
print(s)


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)