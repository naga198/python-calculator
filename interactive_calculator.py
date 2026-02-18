from calculator import Calculator

calc = Calculator()

print("\n" + "="*60)
print("INTERACTIVE CALCULATOR - Financial Functions")
print("="*60 + "\n")

while True:
    print("\nOptions:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Internal Rate of Return (IRR)")
    print("4. Basic Operations (Add, Subtract, Multiply, Divide, Modulo)")
    print("0. Exit")
    
    choice = input("\nSelect option (0-4): ").strip()
    
    if choice == "0":
        print("Exiting calculator. Goodbye!")
        break
    
    elif choice == "1":
        try:
            principal = float(input("Enter principal amount: $"))
            rate = float(input("Enter interest rate (% per annum): "))
            time = float(input("Enter time period (years): "))
            si = calc.simple_interest(principal, rate, time)
            print(f"\n✓ Simple Interest = ${si:.2f}")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
    
    elif choice == "2":
        try:
            principal = float(input("Enter principal amount: $"))
            rate = float(input("Enter interest rate (% per annum): "))
            time = float(input("Enter time period (years): "))
            compounds = input("Compounds per year (default 1): ").strip()
            compounds = int(compounds) if compounds else 1
            ci = calc.compound_interest(principal, rate, time, compounds)
            total = principal + ci
            print(f"\n✓ Compound Interest = ${ci:.2f}")
            print(f"✓ Total Amount = ${total:.2f}")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
    
    elif choice == "3":
        try:
            print("Enter cash flows (press Enter twice when done):")
            print("Example: -1000 (investment), then 400, 300, 300 (returns)")
            cash_flows = []
            count = 1
            while True:
                cf_input = input(f"Cash flow {count}: $").strip()
                if cf_input == "":
                    if count > 1:
                        break
                    else:
                        print("❌ Please enter at least one cash flow.")
                        continue
                cash_flows.append(float(cf_input))
                count += 1
            
            irr = calc.irr(cash_flows)
            print(f"\n✓ Cash Flows: {cash_flows}")
            print(f"✓ IRR = {irr*100:.2f}%")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
    
    elif choice == "4":
        try:
            print("\nBasic Operations:")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            print(f"\n  Add:      {a} + {b} = {calc.add(a, b)}")
            print(f"  Subtract: {a} - {b} = {calc.subtract(a, b)}")
            print(f"  Multiply: {a} × {b} = {calc.multiply(a, b)}")
            print(f"  Divide:   {a} ÷ {b} = {calc.divide(a, b)}")
            print(f"  Modulo:   {a} % {b} = {calc.modulo(a, b)}")
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
    
    else:
        print("❌ Invalid option. Please select 0-4.")

print("\n" + "="*60 + "\n")
