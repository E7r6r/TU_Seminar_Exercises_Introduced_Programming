class Employee:
    def __inti__(self ,name: str , age: int ,salary:float  ):
        self.name = name 
        self.age = age 
        self.salary = salary 

def  __str__ (self )-> str :
    return f"Name: {self.name},Age: {self.age}, Salary: {self.salrary:.2f} "

def add_manager (employees , name,age ,salary,department):
    manager = Manager(name,age,salary,department)
    employees.append(manager)

def add_salesperson (employees , name,age ,salary,sales_target):
    from SalesPerson import SalesPerson
    salesperson = SalesPerson(name,age,salary,sales_target)
    employees.append(salesperson)
def print_employee_info(employees,employee_type = "all"):
    print("\n information for workers:\n")                                         