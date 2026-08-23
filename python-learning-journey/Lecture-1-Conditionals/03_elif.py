weight = float(input("Weight (kg): "))
if weight >= 50:
  print("Heavy shipment")
elif weight >= 20:
  print("Standard shipment")
else:
  print("Light shipment")