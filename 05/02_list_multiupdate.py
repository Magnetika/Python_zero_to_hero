yearly_salary_list = [50000, 55000, 60000, 65000, 70000, 75000, 80000]
update_salary_values = [52000, 58000, 62000]
update_from_index = 2
update_count = 2
updated_list_index = 0
update_index_stop = update_from_index + update_count

for i in range(update_from_index, update_index_stop):

    yearly_salary_list[i] = update_salary_values[updated_list_index]
    updated_list_index += 1

print(yearly_salary_list)
