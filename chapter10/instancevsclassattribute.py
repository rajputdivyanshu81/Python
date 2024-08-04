# instamce attribute take over class attribute during the assignment retrieval


class Employee:
    language = "Py"
    salary = 120000

harry = Employee()
harry.language = "javascript"
print(harry.salary,harry.language)

# language sets to the javacsript

