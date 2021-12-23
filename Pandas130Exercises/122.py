import pandas as pd


employees = pd.DataFrame({
    'emp_id': ['1001', '1002', '1003', '1004'],
    'first_name': ['John', 'Mark', 'Bob', 'Alice'],
    'last_name': ['Smith', 'Cook', 'Cat', 'Lee'],
    'dept_id': ['002', '001', '001', '005']
})

departments = pd.DataFrame({
    'dept_id': ['001', '002', '003', '004'],
    'dept_name': ['IT', 'Sales', 'Marketing', 'Support']
})

print(pd.merge(employees, departments, how='left', on='dept_id'))