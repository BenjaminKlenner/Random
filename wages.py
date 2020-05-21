#define variables
rate = float(input("What is your hourly rate, enter '0' for minimum wage "))
hours = float(input("How many hours did you work this last week? "))

#Validate variables
if rate < 0:
    print("Amount of hours worked can't be less than 0, you entered ${}".format(hours))
    exit()
if rate == 0:
    rate = 18.90

if hours < 0:
    print("{} hours is an invalid value".format(hours))
    exit()
    
#calculate pay
pay = rate * hours
yearly_pay = pay * 52

#Kiwisaver calculation
kiwisaver = float(input("What kiwisaver rate are you on?\n0%\n3%\n4%\n6%\n8%\n10%\n"))
if kiwisaver != 0 and kiwisaver != 3 and kiwisaver != 4 and kiwisaver != 6 and kiwisaver != 8 and kiwisaver != 10:
    print("Invalid rate")

kiwisaver_amount = kiwisaver * pay / 100
pay_after_kiwisaver = pay - kiwisaver_amount
yearly_pay_after_kiwisaver = yearly_pay - kiwisaver_amount * 52

#tax code M calculation
if yearly_pay <= 14000:
    tax_rate = 11.89
elif yearly_pay <= 48000:
    tax_rate = 18.89
elif yearly_pay <= 70000:
    tax_rate = 31.39
else:
    print("Unable to calculate tax")
    exit()
    
pay_after_tax = pay_after_kiwisaver - (tax_rate * pay_after_kiwisaver / 100)
yearly_pay_after_tax = yearly_pay_after_kiwisaver - (tax_rate * yearly_pay_after_kiwisaver / 100)
tax_paid = tax_rate * pay_after_kiwisaver / 100
yearly_tax_paid = tax_rate * yearly_pay_after_kiwisaver / 100
deductions = tax_paid + kiwisaver_amount

#final statments
print("Hourly Rate: ${}\nHours worked: {}\nPay before tax: ${}\nTax rate: {}%\nPay after tax: ${}\nTax Paid: ${}\nAmount given to Kiwisaver: ${}\nYearly projected income before tax: ${}\nYearly projected income after tax: ${}\nYearly projected tax paid: ${}\nTotal deductions: ${}".format(rate,hours,pay,tax_rate,pay_after_tax,tax_paid,kiwisaver_amount,yearly_pay,yearly_pay_after_tax,yearly_tax_paid,deductions))

