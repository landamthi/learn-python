import datetime

def ask_yes_anwer(prompt):
	while True:
		answer = input(prompt)
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		else:
			continue
def calculate_age(year_born):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - year_born
	
def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.128
	feet = meter * METER_TO_FEET
	feet = round(feet,1) # Round decimal numbers 1
	return feet

def print_male(is_male, height_feet):
	if is_male == False:
			if height_feet > 5.7:
				print("You are ",end=" ")
				#-----
				#print("very " *10)
				for i in range(10):
					print("very", end=" ")
				#-----
				print("tall a woman")
			else:
				print("You are short as a woman")
	if is_male == True:
			if height_feet > 6.0:
				print("You are tall as a man")
			#------
			elif height_feet < 5.0:
				print("You are", end=" ")
				i = 0
				while i<10:
					print("short", end=" ")
					i+=1
				print("short a man")
			#------
			else:
				print("You are short as a man")

def print_information( lastname, firstname, age, is_VietNam, height_feet, is_male ):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	print("\n----")
	print("You are height feet " + str(height_feet) + " feet tall")
	print("Your name is " + firstname + " " + lastname)
	print("{2} are {0} year old in {1}".format(age,CURRENT_YEAR,firstname))
	if is_VietNam == True:
		print("You are from VietNam")
	else:
		print("You are not from VietNam")
	print_male(is_male, height_feet)

def ask_person_info():
	# ask for details from users 
	firstname = input("Your firstname:  ")
	lastname = input("Your lastname: ")
	year_born = int(input("When you were born: "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_anwer("Are you male (yes/no): ")
	is_VietNam = ask_yes_anwer("Are you VietNam (yes/no): ")
	return firstname, lastname, year_born, height_meter, is_male, is_VietNam 

def main():
	firstname, lastname, year_born, height_meter, is_male, is_VietNam = ask_person_info()
	#print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
	age = calculate_age(year_born)
	height_feet = convert_meter_to_feet(height_meter)
	print_information( lastname, firstname, age, is_VietNam, height_feet, is_male)
	
main()


		
