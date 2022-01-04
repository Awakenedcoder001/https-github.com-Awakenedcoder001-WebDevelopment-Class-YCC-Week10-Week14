class EmployeeDetails:
    @staticmethod
    def static_variable():
        EmployeeDetails.company_name="TCC"
        print(f"Name of the company is : {EmployeeDetails.company_name}")

customer1=EmployeeDetails()
#calling static method using object reference
customer1.static_variable()
print(EmployeeDetails.__dict__)


