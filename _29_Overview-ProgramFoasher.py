def calc_total_price(apple_weight, APPLE_PRICE):
	return APPLE_PRICE * apple_weight

def calc_return(total_price, money_given):
	# if money_given - total_price < -1 :
	# 	return -1
	# return money_given - total_price
	
	if money_given < total_price:
		return -1
	return money_given - total_price



def print_return_info(total):
	count_500 = int (total/500)
	total = total - 500*count_500
	if count_500 != 0:
		print("500: " + str(count_500))

	count_200 = int (total/200)
	total = total - 200*count_200
	if count_200 != 0:
		print("200: " + str(count_200))

	count_100 = int (total/100)
	total = total - 100*count_100
	if count_100 != 0:
		print("100: " + str(count_100))

	count_50 = int (total/50)
	total = total - 50*count_50
	if count_50 != 0:
		print("50: " + str(count_50))

	count_20 = int (total/20)
	total = total - 20*count_20
	if count_20 != 0:
		print("20: " + str(count_20))

	count_10 = int (total/10)
	total = total - 10*count_10
	if count_10 != 0:
		print("10: " + str(count_10))

	count_1 = total
	if count_1 != 0:
		print("1: " + str(int(count_1)))

def main():
	APPLE_PRICE = 21     # K VND
	apple_weight = input("Enter weght of apples: ")
	money_given = input("Total money customer give you: ")

	apple_weight = float(apple_weight)
	money_given = float(money_given)

	total_price = calc_total_price(apple_weight, APPLE_PRICE)
	money_return = calc_return(total_price, money_given)

	print("Total price: " + str(round(total_price,3)))
	if money_return == -1:
		print("Not enough cash")
	else:
		print("You need to return to customer: " + str(round(money_return,3)) + "K VND")
		print_return_info(money_return)

main()


	

