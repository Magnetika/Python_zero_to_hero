yearly_salary = (50000, 60000, 70000, 80000, 90000)
yearly_salary_list = list(yearly_salary)
print(type(yearly_salary_list))

yearly_salary_list[2] = 75000
modified_yearly_salary = tuple(yearly_salary_list)
print(modified_yearly_salary)
print(type(modified_yearly_salary))
# Output: <class 'tuple'>