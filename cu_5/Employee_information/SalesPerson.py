class SalesPerson(Employee):
   def __init__(self, name, age, salary, sales_target):
        super().__init__(name, age, salary)
        self.sales_target = sales_target   