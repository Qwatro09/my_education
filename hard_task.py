my_answer = {}
list_grades = []

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students) # переводим множество в список и сортируем его
list_students.sort()

for i_num in grades: # ищем среднее арифметическое оценок и сохраняем его в отдельный список
    i_sum = (sum(i_num) / len(i_num))
    list_grades.append(i_sum)

for j_num in range(len(list_grades)): # создаем словарь из двух списков
    my_answer.update({list_students[j_num]:list_grades[j_num]})
print(my_answer)