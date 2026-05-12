import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, abs(a))
        return result if (a >= 0 and b >= 0) or (a < 0 and b < 0) else -result

    def divide(self, a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b
    
    def modulo(self, a, b):
        return a % b

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        if number < 0:
            raise ValueError('Cannot calculate square root of negative number')
        return math.sqrt(number)

    def percentage(self, value, total):
        return (value / total) * 100

    def simple_interest(self, principal, rate, time):
        return (principal * rate * time) / 100
    
    def compound_interest(self, principal, rate, time, compounds_per_year=1):
        rate_decimal = rate / 100
        amount = principal * ((1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time))
        return amount - principal

    def emi(self, principal, annual_rate, tenure_years):
        monthly_rate = annual_rate / (12 * 100)
        months = tenure_years * 12
        emi_value = principal * monthly_rate * ((1 + monthly_rate) ** months)
        emi_value /= (((1 + monthly_rate) ** months) - 1)
        return round(emi_value, 2)

    def sip_returns(self, monthly_investment, annual_rate, years):
        monthly_rate = annual_rate / (12 * 100)
        months = years * 12
        future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
        return round(future_value, 2)

    def cagr(self, beginning_value, ending_value, years):
        return round((((ending_value / beginning_value) ** (1 / years)) - 1) * 100, 2)
    
    def irr(self, cash_flows, guess=0.1, max_iterations=100, tolerance=1e-6):
        def npv(rate, flows):
            npv_value = 0
            for t, cf in enumerate(flows):
                npv_value += cf / ((1 + rate) ** t)
            return npv_value
        
        def npv_derivative(rate, flows):
            derivative = 0
            for t, cf in enumerate(flows):
                if t > 0:
                    derivative -= t * cf / ((1 + rate) ** (t + 1))
            return derivative
        
        rate = guess
        for _ in range(max_iterations):
            npv_val = npv(rate, cash_flows)
            if abs(npv_val) < tolerance:
                return rate
            
            npv_deriv = npv_derivative(rate, cash_flows)
            if abs(npv_deriv) < tolerance:
                break
            
            rate = rate - npv_val / npv_deriv
        
        return rate

if __name__ == '__main__':
    calc = Calculator()
    print('Advanced Finance & Scientific Calculator')
    print('Addition:', calc.add(10, 5))
    print('Power:', calc.power(2, 5))
    print('Square Root:', calc.square_root(64))
    print('EMI:', calc.emi(500000, 8.5, 10))
    print('SIP Returns:', calc.sip_returns(5000, 12, 10))