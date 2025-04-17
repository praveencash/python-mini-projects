import time
duration = int(input('Enter the number of seconds to run : '))
print(f'\nCountdown set for {duration} seconds\n')
print('Starting', end='')
for _ in range(3):
	time.sleep(0.5)
	print('.', end='')
print('\n')
for i in range(duration, 0, -1):
	print(i)
	time.sleep(1)
print("Time is up!\n" + "-" * 20)
	
