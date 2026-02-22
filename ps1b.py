annual_salary=float(input("Enter your starting annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save,as a decimal:"))
total_cost=float(input('Enter the cost of your dream house:'))
semi_annual_raise=float(input("Enter the semi annual raise,as a decimal:"))
#down payment
down_payment=0.25*total_cost 
current_savings=0.0
annual_return=0.04
#current monthly salary
monthly_salary=annual_salary/12
monthly_saving=portion_saved*monthly_salary
#monthly return rate
r=0.04/12
months=0
while current_savings<down_payment:
    current_savings+=monthly_saving+(current_savings*r)
    months+=1
    if months%6==0:
        annual_salary+=annual_salary*semi_annual_raise
        monthly_salary=annual_salary/12
print(f"Number of months:{months}")


