 my_list = ["abc", 123, "xyz"]
 for i in range(0, len(my_list)):
     print(i, my_list[i])
  output: 0 abc, 1 123, 2 xyz
    
# OR 
    
# for key in my_list:
#     print(key)
# output: abc, 123, xyz
# for i in range(0, len(my_list)):
#     print(i, my_list[i])


dojo_student = [
        {"first_name": "Houssem", "last_name": "Bahri"},
        {"first_name": "Ghaith", "last_name": "Ouni"},
        {"first_name": "Yaya", "last_name": "Dembele"}
    ]
for i in range(0, len(dojo_student)):
    print(i, dojo_student[i])



for count in range(0,5):
    print("looping =", count)



count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

