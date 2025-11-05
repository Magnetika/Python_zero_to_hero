programming_language = 'Java'
is_scripting_language = True

if programming_language == 'Java' and is_scripting_language:
    print('Javascript')
else:
    print('Is not Java or not a scripting language')

if programming_language == 'Java' or programming_language == 'Python':
    print('Backend language')

backend_languages = ['Java', 'Python', 'C#', 'Ruby', 'Go']
if programming_language in backend_languages:
    print('Backend language')   