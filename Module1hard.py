grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = sorted(students)
average_0=sum(grades[0])/len(grades[0])
average_1=sum(grades[1])/len(grades[1])
average_2=sum(grades[2])/len(grades[2])
average_3=sum(grades[3])/len(grades[3])
average_4=sum(grades[4])/len(grades[4])
print({list_students[0]:average_0,list_students[1]:
average_1,list_students[2]:average_2,list_students[3]:
average_3,list_students[4]:average_4})