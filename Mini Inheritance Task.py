class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def show_details(self):
		print(self.name)
		print(self.age)
class student(person):
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self.grade = grade
	def show_grade(self):
		print(self.grade)
class teacher(person):
	def __init__(self, name, age, subject):
		super().__init__(name, age)
		self.subject = subject
	def show_subject(self):
		print(self.subject)	
		
s1 = student("Meena", 18, "A")
t1 = teacher("Mr. Raj", 40, "Math")

s1.show_details()
s1.show_grade()

t1.show_details()
t1.show_subject()	