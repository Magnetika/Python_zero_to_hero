yearly_salary_list = [50000, 60000, 55000, 70000, 65000]
yearly_salary_list_copy = yearly_salary_list.copy()  # This creates a shallow copy of the list

print('yearly_salary_list:', yearly_salary_list)
print('yearly_salary_list_copy:', yearly_salary_list_copy)
print('yearly_salary_list memory address:', id(yearly_salary_list))
print('yearly_salary_list_copy memory address:', id(yearly_salary_list_copy))
# Modify the copy by adding a bonus to each salary
for i in range(len(yearly_salary_list_copy)):
    yearly_salary_list_copy[i] += 5000  # Adding a bonus of 5000 to each salary
print("Modified Yearly Salary List Copy:", yearly_salary_list_copy)
# Original list remains unchanged because we modified the copy  
print("Original Yearly Salary List after modification of copy:", yearly_salary_list)
# This code demonstrates how to create a copy of a mutable object (like a list) in Python.
# Calculate the total yearly salary from the copied list
total_yearly_salary_copy = sum(yearly_salary_list_copy)
print("Total Yearly Salary from Copy:", total_yearly_salary_copy)
# Calculate the total yearly salary from the original list
total_yearly_salary_original = sum(yearly_salary_list)
print("Total Yearly Salary from Original:", total_yearly_salary_original)
# Append a new salary to the original list  
yearly_salary_list.append(80000)
print('After appending a new salary to yearly_salary_list:')
print('yearly_salary_list:', yearly_salary_list)
print('yearly_salary_list_copy (should be unchanged):', yearly_salary_list_copy)
print('After appending a new salary to yearly_salary_list:')
print('yearly_salary_list:', yearly_salary_list)    
print('yearly_salary_list_copy (should be unchanged):', yearly_salary_list_copy)






