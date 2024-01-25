

def main():
	CURRENT_YEAR = 2024
	METER_TO_FEET = 3.128

	firstname = input("Your firstname:  ")
	lastname = input("Your lastname: ")
	year_born = input("When you were born: ")
	height_meter = input("Your height (meter): ")


	#print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
	#height

	year_born = int(year_born)
	age = CURRENT_YEAR - year_born

	height_meter = float(height_meter)
	height_feet = height_meter * METER_TO_FEET
	height_feet = round(height_feet,1) # Round decimal numbers 1

	print("\n----")
	print("You are height feet " + str(height_feet) + " feet tall")
	print("Your name is " + firstname + " " + lastname)
	print("{2} are {0} year old in {1}".format(age,CURRENT_YEAR,firstname))

	gender_input = input("You are male (yes/no): ")
	is_male = None
	if (gender_input == "yes") or (gender_input == "y") or (gender_input == "Yes"):
		is_male = True
	elif (gender_input == "no") or (gender_input == "n") or (gender_input == "No"):
		is_male = False
	else :
		is_male = None

	if is_male is None:
		print("Invalid awser")
	elif is_male == False:
			if height_feet > 5.7:
				print("You are tall as a woman")
			else:
				print("You are short as a woman")
	elif is_male == True:
			if height_feet > 6.0:
				print("You are tall as a man")
			else:
				print("You are short as a man")
	else:
		print("System error: Variable is 'is_male' not a correct")
		
