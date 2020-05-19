#define variables
rate = float(input("What is your hourly rate, enter '0' for minimum wage "))
hours = float(input("How many hours did you work this last week? "))

#calculate pay and display
if rate == 0:
    rate = 18.90

pay = rate * hours
print("At an hourly rate of ${} an hour, you will be paid: ${} before tax.".format(rate,pay))

#Projected yearly income calculation
yearly_pay = pay * 52



#tax code M calculation
if yearly_pay <= 14000:
    tax_rate = 11.89
elif yearly_pay <= 48000:
    tax_rate = 18.89
elif yearly_pay <= 70000:
    tax_rate = 31.39
else:
    print("Unable to calculate tax")
pay_after_tax = tax_rate * pay / 100
yearly_pay_after_tax = tax_rate * yearly_pay / 100


#final statments
print("With a projected yearly income of ${}, you will be taxed at {}%".format(yearly_pay,tax_rate))
print("Weekly, after tax, you will get: ${}".format(pay_after_tax))
print("With a yearly total, after tax, of: ${}".format(yearly_pay_after_tax))
