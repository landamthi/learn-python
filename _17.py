s_denomonator = 0

for i in range(100):
	if i == 1:
		continue

	if i % 2 == 0:
		continue

	s_denomonator += 1/i

s = 1/s_denomonator
s = round(s,3)
print("S = " + str(s))

