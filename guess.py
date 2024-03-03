import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input ('請猜數字: ')
	num = int(num)
	if num != r and num < r:
		print('比答案還要小喔!')
	elif num != r and num > r:
		print('比答案還要大喔!')
	else:
		num == r
		print('終於猜對了!')
		print('你總共猜了',count ,'次')
		break
	print('這是你猜的第', count, '次')