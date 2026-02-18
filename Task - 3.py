import pandas as pd

try:
    df = pd.read_csv('data.csv')
    print("Data read from file (first 5 rows):")
    print(df.head())
    print("-" * 30)

except FileNotFoundError:
    
    print("data.csv not found. Creating a sample DataFrame for demonstration.")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Department': ['HR', 'Marketing', 'IT', 'Marketing', 'HR'],
        'Salary': [50000, 60000, 55000, 70000, 52000],
        'Age': [25, 30, 35, 40, 28]
    }
    df = pd.DataFrame(data)
    print("Sample DataFrame:")
    print(df)
    print("-" * 30)

filtered_salary_df = df[df['Salary'] > 55000]
print("Filtered by Salary > 55000:")
print(filtered_salary_df)
print("-" * 30)


departments_to_keep = ['HR', 'IT']
filtered_department_df = df[df['Department'].isin(departments_to_keep)]
print("Filtered by Department in ['HR', 'IT']:")
print(filtered_department_df)
print("-" * 30)

filtered_query_df = df.query('Salary > 55000 and Department == "Marketing"')
print("Filtered using query('Salary > 55000 and Department == \"Marketing\"'):")
print(filtered_query_df)
print("-" * 30)

filtered_loc_df = df.loc[df['Age'] > 30, ['Name', 'Salary']]
print("Filtered using .loc[df['Age'] > 30, ['Name', 'Salary']]:")
print(filtered_loc_df)
print("-" * 30)
