yearly_salary_list = [50000, 60000, 55000, 70000, 65000]
sum_high_salary = 0
sum_low_salary = 0

for salary in yearly_salary_list:
    if salary > 60000:
        sum_high_salary += salary
    else:
        sum_low_salary += salary

print("Total high salary:", sum_high_salary)
print("Total low salary:", sum_low_salary)
