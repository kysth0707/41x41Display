def CustomConverter(num : int):
	digit = 2**16
	number = num
	ExportTxt = ""

	if number == 0:
		return "000"
	
	while(number != 0):
		remain = number % digit

		if remain > 9:
			ExportTxt = chr(97 + remain - 10) + ExportTxt
		else:
			ExportTxt = str(remain) + ExportTxt
		
		number = int(number / digit)
		# print(number)

	return ExportTxt.zfill(3)

# print(CustomConverter(16, 729))