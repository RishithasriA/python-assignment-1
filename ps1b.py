annual_salary=float(input("enter your starting annual salary:"))
portion_saved=float(input("enter the pecent of your salary to save,as a decimal:"))
total_cost=float(input('enter the cost of your dream house:'))
semi_annual_raise=float(input("enter the semi annual raise,as adecimal:"))
#down patment
down_payment=0.25*total_cost 
current_savings=0.0
#current monthly salary
monthly_salary=annual_salary/12
monthly_saving=portion_saved*monthly_salary
#monthly return rate
r=0.04/12
months=0
while current_savings<down_payment:
    current_savings+=monthly_saving+(current_savings*r)
    months+=1
print(f"number of months:{months}")