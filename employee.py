"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, commission, com_freq):
        self.name = name
        self.salary = salary
        self.commission = commission
        self.com_freq = com_freq
        self.total_pay = 0

    def get_pay(self): 
        self.total_pay = self.salary + (self.commission * self.com_freq)
        return self.total_pay

    def __str__(self):
        if self.commission == 0:
            print(self.name, "works on a monthly salary of", str(self.salary) + ". Their total pay is", str(self.total_pay) + ".")
        elif self.com_freq == 1:
            print(self.name, "works on a monthly salary of", self.salary, "and receives a bonus commission of", str(self.commission) +  ". Their total pay is", str(self.total_pay) + ".")
        else:
            print(self.name, "works on a monthly salary of", self.salary, "and receives a commission for", self.com_freq, "contract(s) at", str(self.commission) + "/contract. Their total pay is", str(self.total_pay) + ".")
        return self.name

class Contract(Employee):
    def __init__(self, name, salary, commission, com_freq, hours):
        super().__init__(name, salary, commission, com_freq)
        self.hours = hours
    
    def get_pay(self):
        self.total_pay = (self.salary * self.hours) + (self.commission * self.com_freq)
        return self.total_pay

    def __str__(self):
        if self.commission == 0:
            print(self.name, "works on a contract of", self.hours, "hours at", str(self.salary) + "/hour. Their total pay is", str(self.total_pay) + ".")
        elif self.com_freq == 1:
            print(self.name, "works on a contract of", self.hours, "hours at", str(self.salary) + "/hour and receives a bonus commission of", str(self.commission) + ". Their total pay is", str(self.total_pay) + ".")
        else:
            print(self.name, "works on a contract of", self.hours, "hours at", str(self.salary) + "/hour and receives a commission for", self.com_freq, "contract(s) at", str(self.commission) + "/contract. Their total pay is", str(self.total_pay) + ".")
        return self.name

    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 0, 0)
billie.get_pay()
str(billie)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Contract('Charlie', 25, 0, 0, 100)
charlie.get_pay()
str(charlie)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 200, 4)
renee.get_pay()
str(renee)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Contract('Jan', 25, 220, 3, 150)
jan.get_pay()
str(jan)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 1500, 1)
robbie.get_pay()
str(robbie)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Contract('Ariel', 30, 600, 1, 120)
ariel.get_pay()
str(ariel)