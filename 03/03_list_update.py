yearly_salary_list = [50000, 60000, 55000, 70000, 65000]

yearly_salary_list[0] = 58000  # Update the first employee's salary

print(yearly_salary_list)  # Output the updated list

del yearly_salary_list[2]  # Remove the third employee's salary

print(yearly_salary_list)  # Output the list after deletion

yearly_salary_list.append(72000)  # Add a new employee's salary

print(yearly_salary_list)  # Output the final list  

yearly_salary_list.extend([68000, 75000])  # Add multiple new salaries

print(yearly_salary_list)  # Output the list after extending

yearly_salary_list.insert(2, 59000)  # Insert a salary at index 2

print(yearly_salary_list)  # Output the list after insertion    

yearly_salary_list.remove(65000)  # Remove the salary of 65000

print(yearly_salary_list)  # Output the list after removing the salary  