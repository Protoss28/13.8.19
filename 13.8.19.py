ticket = int(input('Number of tickets'))

if ticket <= 0 or ticket > 100:
    print("Tickets must be more than 0 and less than 100")
else: 
    age = [ticket]

sum = 0
for i in range(len(age)):
		 age[i] = int(input('Age of participants? ' + (i+1)))
if 18 <= age[i] <= 25:
			sum = sum + 990
elif age[i] > 25:
			sum = sum + 1390
if ticket > 3 :
		 sum = sum * 0.9
print("Total amount: " + round(sum, 2))