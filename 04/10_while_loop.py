 #while 1:
while True:
    grade = input('Enter your grade: ')
    if grade.isdigit() and 0 < int(grade) < 6:
        print('This is a grade')
        break
    print('This is not a grade, try again')
    
        