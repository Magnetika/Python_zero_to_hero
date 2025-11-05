yearly_salary_list = [50000, 55000, 60000, 65000, 70000, 75000, 80000]
print('from the 2', yearly_salary_list[2:])  # Slicing from index 2 to the end
print('to the 2' , yearly_salary_list[:2])    # Slicing from the start to index 2 (exclusive)
print('between 2 and 5', yearly_salary_list[2:5])  # Slicing from index 2 to index 5 (exclusive)
print('last 3 elements', yearly_salary_list[-3:])  # Slicing the last 3 elements
print('all but last 2 elements', yearly_salary_list[:-2])  # Slicing all but the last 2 elements
print('every second element', yearly_salary_list[::2])  # Slicing with a step of 2  