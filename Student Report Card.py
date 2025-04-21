class student:
	def __init__(self, name, subject1, subject2, subject3):
		self.name = name
		self.subject1 = subject1
		self.subject2 = subject2
		self.subject3 = subject3
	def calculate_average(self):
		average = (self.subject1 + self.subject2 + self.subject3)/3
		return average
	def get_grade(self):
		avg = self.calculate_average()
		if avg >= 90:
			return 'A'
		elif avg >= 75:
			return 'B'
		elif avg >= 50:
			return 'C'
		else:
			return 'F'
	def show_report(self):
		print('Name:', self.name)
		print('Scores:', self.subject1, self.subject2, self.subject3)
		print('Average scores:', self.calculate_average())
		print('Grade:', self.get_grade())
		
s1 = student("Praveen", 85, 74, 90)
s1.show_report()
		
		
		