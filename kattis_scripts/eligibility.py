no = int(input())

'''
a simple if else condition to look if a student is eligible.
conditions are either based on enrolled date, birthdate and the number of courses already taken

'''

for i in range(no):
    name, start_date, birth_date, courses_no = input().split()
    if int(start_date[0:4]) >= 2010:
        print(name + ' eligible')
    elif int(birth_date[0:4]) >= 1991:
        print(name + ' eligible')
    elif int(courses_no) >= 41:
        print(name + ' ineligible')
    else:
        print(name + ' coach petitions')
