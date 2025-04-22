class animal:
	def make_sound(self):
		print('Some animal sound')
class dog(animal):
	def make_sound(self):
		print('Woof!')
class cat(animal):
	def make_sound(self):
		print('Meow!')
dog1 = dog()
cat1 = cat()
dog1.make_sound()
cat1.make_sound()