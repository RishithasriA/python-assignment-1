# python-assignment-1
#ps1a.py
annual_salary=float(input("enter yourannual salary:"))
portion_saved=float(input("enter the percent of your salary to save , as a decimal :"))
cost_of_dreamhouse=float(input("enter thecost of your dream house :"))
#down_payment(25% of total_cost)
down_payment=0.25*cost_of_dreamhouse
current_savings=0.0
#monthly income
monthly_salary=annual_salary/12
#monthly savings
monthly_saving=portion_saved*monthly_salary
#monthly return rate(4% annual)
r=0.04/12
months=0
while current_savings<down_payment:
    current_savings+=monthly_saving+(current_savings*r)
    months+=1
print(f'number of montha:{months}') 



#ps1b.py

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




