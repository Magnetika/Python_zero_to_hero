yearly_salary_list = [50000, 60000, 85000, 70000, 15000]
high_salary_limit = 60000

for i in yearly_salary_list:
    if i > high_salary_limit:
        continue
    print(i)

for i in yearly_salary_list:
    if i <= high_salary_limit:
        print(i)    