def CustomConverter(digit : int, num : int):
	number = num
	ExportTxt = ""

	if number == 0:
		return number
	
	while(number != 0):
		remain = number % digit

		if remain > 9:
			ExportTxt = chr(97 + remain - 10) + ExportTxt
		else:
			ExportTxt = str(remain) + ExportTxt
		
		number = int(number / digit)
		# print(number)

	return ExportTxt

# print(CustomConverter(16, 729))