import random
r = random.randint(1, 100)
while True:
	num = input ('請猜數字1~100: ')
	num = int(num)
	if num != r and num < r:
		print('猜錯囉! 比答案還要小喔!')
	elif num != r and num > r:
		print('猜錯囉! 比答案還要大喔!')
	else:
		num == r
		print('終於猜對了!')
		break