import pandas as pd 
 
df = pd.DataFrame({ 
    'Name': ['Alice', 'Bob', 'David'], 
    'Age': [25, 32, 47], 
    'City': ['NY', 'LA', 'NY'], 
    'Salary': [70000, 90000, 120000] 
}) 
print(df) 
 
print(df.head(), df.shape) 
print(df.sort_values('Age')) 
print(df[df['Age'] > 30]) 
dept = pd.DataFrame({ 
    'Name': ['Alice', 'Bob', 'David'], 
    'Dept': ['HR', 'Eng', 'Eng'] 
}) 
merged = pd.merge(df, dept, on='Name') 
print(merged) 
print(df.groupby('City')['Salary'].mean())
