class LoanCalculator:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def monthly_payment(self):
        rate = self.annual_rate / 12 / 100
        n_payments = self.years * 12
        payment = (self.principal * rate) / (1 - (1 + rate) ** -n_payments)
        return payment

    def total_payment(self):
        return self.monthly_payment() * self.years * 12

class SavingsCalculator:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def compound_interest(self):
        rate = self.annual_rate / 100
        amount = self.principal * (1 + rate) ** self.years
        return amount

def main():
    print("Finance Calculator")
    print("1. Loan Calculator")
    print("2. Savings Calculator")
    choice = input("Choose an option: ")

    if choice == "1":
        principal = float(input("Enter loan principal: "))
        annual_rate = float(input("Enter annual interest rate (in %): "))
        years = int(input("Enter loan term (in years): "))
        loan = LoanCalculator(principal, annual_rate, years)
        print("Monthly Payment: ${:.2f}".format(loan.monthly_payment()))
        print("Total Payment: ${:.2f}".format(loan.total_payment()))
    
    elif choice == "2":
        principal = float(input("Enter initial savings amount: "))
        annual_rate = float(input("Enter annual interest rate (in %): "))
        years = int(input("Enter savings term (in years): "))
        savings = SavingsCalculator(principal, annual_rate, years)
        print("Future Value: ${:.2f}".format(savings.compound_interest()))
    
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

