yearly_salary_list = [50000, 60000, 55000, 70000, 65000]
yearly_salary_list_2 = [52000, 62000, 58000, 72000, 68000]

print(yearly_salary_list + yearly_salary_list_2)  # Concatenation of two lists

yearly_salary_lists = yearly_salary_list + yearly_salary_list_2
print(yearly_salary_lists)  # Repetition of the combined list
print(yearly_salary_lists * 2)  # Repetition of the combined list   

print(len(yearly_salary_lists))  # Length of the combined list

print(10000 in yearly_salary_list)  # Membership test (True)

print(50000 in yearly_salary_list)  # Membership test (False)