import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	num = input ('請猜數字1~100: ')
	num = int(num)
	if num != r and num < r:
		print('猜錯囉! 比答案還要小喔!')
	elif num != r and num > r:
		print('猜錯囉! 比答案還要大喔!')
	else:
		num == r
		print('終於猜對了!')
		print('你總共猜了',count ,'次')
		break
	print('這是你猜的第', count, '次')