income = int(input("Enter your INCOME: "))
total_tax = 0

if income <= 300000:
  print("No tax")

else:
  if income <= 600000:
    tax1 = (income - 300000) * 0.05
    total_tax = tax1
  else:
    total_tax += 300000 * 0.05
  if income > 600000:
    if income <= 900000:
      tax2 = (income - 600000) * 0.10
      total_tax += tax2
    else:
      total_tax += 300000 * 0.10
  if income > 900000:
    tax3 = (income - 900000) * 0.15
    total_tax += tax3

  print("Your Total tax is:", int(total_tax))