def age_calc():
	age = 0	
	name = input("your name: ")
	year = int(input("your year: "))

	print("start "+str(age)+" "+str(year))
	for value in range(1, 10000):
		if year<2021:
			age = age+1
			year = year+1
			print(str(age)+" in "+str(year)+"\n")
	print("🇭 🇮  "+"there "+name+" you are: "+str(age)+" years old")
age_calc()