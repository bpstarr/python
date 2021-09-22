# #1.
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0]= 15
# students[0].update({'last_name':'Bryant'})
# sports_directory.update({'soccer': ['Andres','Ronaldo','Rooney']})
# z[0]['y'] = 30


#2.
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    # ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterate_dictionary(students):
#     for x in range(len(students)):
#         print([f"first_name - {students[x]['first_name']}, last_name - {students[x]['last_name']}"])
# iterate_dictionary(students)

# #3.
# def iterate_dictionary2(students):
#     for x in range(len(students)):
#         print(students[x]['first_name'])
# iterate_dictionary2(students)
# def iterate_dictionary3(students):
#     for x in range(len(students)):
#         print(students[x]['last_name'])
# iterate_dictionary3(students)
# Michael
# John
# Mark
# KB

# Jordan
# Rosales
# Guillen
# Tonel

#4.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dojo):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for x in range(len(dojo['locations'])):
        print(dojo['locations'][x])

    print(f"{len(dojo['instructors'])} LOCATIONS")
    for x in range(len(dojo['instructors'])):
        print(dojo['instructors'][x])
print_info(dojo)
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon






