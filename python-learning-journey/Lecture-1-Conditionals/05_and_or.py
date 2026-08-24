weight = float(input("Enter your weight (kg): "))
express_paid = (input("Paid for express?: "))

if weight <= 5 and express_paid:
  print("Express shipping")
else:
  print("Standard shipping")