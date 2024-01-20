CURRENT_YEAR = 2024
METER_TO_FEET = 3.128

# Input
firstname = input("Your firstname:  ")
lastname = input("Your lastname: ")
year_born = input("When you were born: ")
height_meter = input("Your height (meter): ")

#print("You are " + str(age) + " years old in " + str(CURRENT_YEAR))
# Check anser
while True:
	gender_input = input("You are male (yes/no): ")
	if (gender_input == "yes") or (gender_input == "no"):
		break
	
year_born = int(year_born)
age = CURRENT_YEAR - year_born
height_meter = float(height_meter)
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1) # Round decimal numbers 1

print("\n----")
print("You are height feet " + str(height_feet) + " feet tall")
print("Your name is " + firstname + " " + lastname)
print("{2} are {0} year old in {1}".format(age,CURRENT_YEAR,firstname))

#Yes/no
if gender_input == "yes" :
	is_male = True
if gender_input == "no" :
	is_male = False

#if/else

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


		
