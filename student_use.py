from student import Student

# Пример использования:
student = Student("Антон Иванов", "subjects.csv")
student.add_score("Информатика", 5)
student.add_test_result("Информатика", 95)
print(student.average_test_score("Информатика"))
print(student.average_score())