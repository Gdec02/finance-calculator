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

# Example usage
principal = 100000
annual_rate = 5
years = 30
loan = LoanCalculator(principal, annual_rate, years)
print("Monthly Payment: ${:.2f}".format(loan.monthly_payment()))
print("Total Payment: ${:.2f}".format(loan.total_payment()))
