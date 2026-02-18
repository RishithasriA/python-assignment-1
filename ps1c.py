annual_salary = float(input("Enter the starting salary: "))

# Bisection search setup
total_cost = 1000000
down_payment = 0.25 * total_cost  # $250,000
low = 0.0
high = 1.0  # Max 100% savings rate
steps = 0
epsilon = 100  # $100 accuracy
found = False

#Bisection loop
while high - low >= 1e-6:  # High precision
    steps += 1
    mid_rate = (low + high) / 2
    
    savings = calculate_savings (mid_rate, annual_salary)
    
    if abs(savings - down_payment) <= epsilon:
        print(f"Best savings rate: {mid_rate:.4f}")
        print(f"Steps in bisection search: {steps}")
        found = True
        break
    elif savings < down_payment:
        low = mid_rate
    else:
        high = mid_rate

# Impossible case check
if not found:
    # Test with 100% savings
    max_savings = calculate_savings (1.0, annual_salary)
    if max_savings < down_payment:
        print("It is not possible to pay the down payment in three years.")
    else:
        print(f"Best savings rate: {mid_rate:.4f}")
        print(f"Steps in bisection search: {steps}")