class StudentDetails:
    def __init__(self):
        #Accessing the static variables inside the constructor
        print(f"Course of the student it : {student.course}")
        print(f"the course of the student is : {StudentDetails.course}")

    def static_variable(self):

        #Accessing the static variables Inside the Instance Method
        print(f"The course of the student is: {student.course}")
        print(f"The course of the student is: {StudentDetails.course}")
    
s1=StudentDetails()
print(f"Course of the students is : {StudentDetails.course}")


