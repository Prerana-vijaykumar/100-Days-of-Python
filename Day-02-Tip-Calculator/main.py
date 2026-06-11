print("Welcome to tip calculator")
total_bill=float(input("What was the total bill?"))
tip=float(input("How much tip would you like to give? 10,12 or 15?"))
number_of_people=float(input("How many people to split the bill?"))
final_amount=(total_bill+tip)/number_of_people
print("each person should pay :" + str(final_amount))
