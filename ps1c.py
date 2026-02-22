annual_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
down_payment = 0.25 * total_cost
semi_annual_raise = 0.07
r = 0.04 / 12
months = 36

# search between 0 and 10000 (represents 0.0000 to 1.0000)
low = 0
high = 10000
steps = 0
epsilon = 100

# ---------- check if possible ----------
current_savings = 0.0
temp_salary = annual_salary
monthly_salary = temp_salary / 12

for m in range(1, months + 1):
    current_savings += monthly_salary + (current_savings * r)

    if m % 6 == 0:
        temp_salary *= (1 + semi_annual_raise)
        monthly_salary = temp_salary / 12

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")

else:

    while True:
        steps += 1

        mid = (low + high) // 2
        mid_rate = mid / 10000   # convert to decimal

        current_savings = 0.0
        temp_salary = annual_salary
        monthly_salary = temp_salary / 12

        for m in range(1, months + 1):
            monthly_saving = mid_rate * monthly_salary
            current_savings += monthly_saving + (current_savings * r)

            if m % 6 == 0:
                temp_salary *= (1 + semi_annual_raise)
                monthly_salary = temp_salary / 12

        if abs(current_savings - down_payment) <= epsilon:
            print(f"Best savings rate: {mid_rate:.4f}")
            print(f"Steps in bisection search: {steps}")
            break

        elif current_savings < down_payment:
            low = mid
        else:
            high = mid
