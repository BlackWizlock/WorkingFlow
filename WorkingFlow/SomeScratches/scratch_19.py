def palindrome(num):
	if type(num) != int or num < 9:
		return "Not valid"
	else:
		tmp_num = [x for x in str(num)]

		if num % 2 == 0:
			tmp_num[0:len(num)//2].sort
	return True
