yearly_salary_list = [50000, 60000, 58000, 70000, 65000]

# Sort the list in ascending order
yearly_salary_list.sort()
print(yearly_salary_list)  # Output the sorted list

# Reverse the list
yearly_salary_list.reverse()
print(yearly_salary_list)  # Output the reversed list

# Get the index of a specific salary
index = yearly_salary_list.index(58000)
print(index)  # Output the index of the salary

# Count the occurrences of a specific salary
count = yearly_salary_list.count(60000)
print(count)  # Output the count of the salary

# Clear the entire list
yearly_salary_list.clear()
print(yearly_salary_list)  # Output the cleared list

names_list = ["Alice", "Bob", "Charlie", "David"] 
print(names_list)  # Output the original list of names
print(' '.join(names_list))  # Output the names as a single string separated by spaces  

# Join the names into a single string separated by spaces   
joined_names = ' '.join(names_list)
print(joined_names)  # Output the joined names

# Split the joined string back into a list
split_names = joined_names.split(' ')   
print(split_names)  # Output the split names        