# Simple Interest Calculator
# Authorized under Apache License 2.0

def calculate_simple_interest(principal, rate, time):
    """
    Calculates simple interest.
    Formula: SI = (P * R * T) / 100
    """
    interest = (principal * rate * time) / 100
    return interest

def main():
    print("--- Micro-finance Simple Interest Tool ---")
    
    try:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the annual interest rate (in %): "))
        t = float(input("Enter the time period (in years): "))
        
        si = calculate_simple_interest(p, r, t)
        total_amount = p + si
        
        print(f"\nResults:")
        print(f"Total Interest: {si:.2f}")
        print(f"Total Amount to be repaid: {total_amount:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()