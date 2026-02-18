class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a - b
        return a

    def simple_interest(self, principal, rate, time):
        """
        Calculate simple interest.
        SI = (P × R × T) / 100
        
        Args:
            principal: Initial amount
            rate: Interest rate per annum (%)
            time: Time period in years
            
        Returns:
            Simple interest amount
        """
        return (principal * rate * time) / 100
    
    def compound_interest(self, principal, rate, time, compounds_per_year=1):
        """
        Calculate compound interest.
        A = P(1 + r/n)^(nt)
        CI = A - P
        
        Args:
            principal: Initial amount
            rate: Interest rate per annum (%)
            time: Time period in years
            compounds_per_year: Number of times interest compounds per year (default: 1)
            
        Returns:
            Compound interest amount
        """
        rate_decimal = rate / 100
        amount = principal * ((1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time))
        return amount - principal
    
    def irr(self, cash_flows, guess=0.1, max_iterations=100, tolerance=1e-6):
        """
        Calculate Internal Rate of Return (IRR) using Newton-Raphson method.
        
        Args:
            cash_flows: List of cash flows (first is typically negative investment)
            guess: Initial guess for IRR (default: 0.1 or 10%)
            max_iterations: Maximum iterations for convergence
            tolerance: Convergence tolerance
            
        Returns:
            Internal Rate of Return as a decimal (multiply by 100 for percentage)
        """
        def npv(rate, flows):
            """Calculate Net Present Value at given rate"""
            npv_value = 0
            for t, cf in enumerate(flows):
                npv_value += cf / ((1 + rate) ** t)
            return npv_value
        
        def npv_derivative(rate, flows):
            """Calculate derivative of NPV (for Newton-Raphson)"""
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

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))