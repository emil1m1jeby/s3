import pandas as pd

# Create a pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing columns
print("Names:", df['Name'])
print("Ages:", df['Age'])

