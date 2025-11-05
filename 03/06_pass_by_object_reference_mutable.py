yearly_salary_list = [50000, 60000, 55000, 70000, 65000]
# Calculate the total yearly salary
yearly_salary_list_copy = yearly_salary_list  # This creates a reference to the same list
total_yearly_salary = sum(yearly_salary_list_copy)
print(yearly_salary_list)
print(yearly_salary_list_copy)
print("Total Yearly Salary:", total_yearly_salary)
# Modify the copy by adding a bonus to each salary
for i in range(len(yearly_salary_list_copy)):
    yearly_salary_list_copy[i] += 5000  # Adding a bonus of 5000 to each salary 
print("Modified Yearly Salary List:", yearly_salary_list_copy)
# Original list is also modified because both variables reference the same list
print("Original Yearly Salary List after modification:", yearly_salary_list)
# This code demonstrates how mutable objects (like lists) are passed by reference in Python.

print('yearly_salary_list memory adress', id(yearly_salary_list))
print('yearly_salary_list_copy memory adress', id(yearly_salary_list_copy))

yearly_salary_list.append(80000)
print('After appending a new salary to yearly_salary_list:')
print('yearly_salary_list:', yearly_salary_list)