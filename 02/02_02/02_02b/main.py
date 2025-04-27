''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

#declaring variables is imp, even if python doesn't think so
#creating and initializing a list with values
student_pet_count_list: list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]
#you can technically put different data types in the same list, but it's discouraged
#collections are used for data of sim types

num_students = len(student_pet_count_list)
print(num_students)
#average = sum / num

#square brackets gives index for a list
index_three = student_pet_count_list[3]