yearly_salary  = (50000, 60000, 70000, 80000, 90000)

for i in yearly_salary:
    print(i)

for i in range(len(yearly_salary)):
    print(f"index {i}, value:{yearly_salary[i]}")

for i, v in enumerate(yearly_salary):
    print(f"index {i}, value:{v}")