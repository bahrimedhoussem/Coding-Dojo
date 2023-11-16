x = [ [5,2,3], [10,8,9] ]
x[1][0]=15 

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
print(students)

students[0]['last_name']='Bryant'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='andrea'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for students in some_list:
        print(f"first_name - {students['first_name']}, last_name - {students['last_name']}") 

iterateDictionary(students)

def iterateDictionary2(some_list):  
    for students in some_list:
        print(f"first_name - {students['first_name']}")

iterateDictionary2( students)
def iterateDictionary2(some_list):
    for students in some_list:
        print(f"last_name-{students['last_name']}")
iterateDictionary2(students)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key.upper()}")
        for value in values:
            print(value)
        print() 
printInfo(dojo)        



