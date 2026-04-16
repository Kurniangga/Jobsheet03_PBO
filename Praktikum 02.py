class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def update_salary(self, increase):
        if increase>0:
            self.__salary += increase
            print(f"Gaji telah dinaikkan sebesar {increase}.")
        else:
            print("Nilao kenaikkan gaji harus lebih dari 0.")
            
    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Gaji diatur ulang menjadi {new_salary}.")
        else:
            print("Gaji tidak dapat bernilai negatid.")

    def get_salary(self):
        return self.__salary
    
    def get_employee_info(self):
        return f"Employee: {self.__name}, Gaji: {self.__salary}."

if __name__ == "__main__":
    employee1 = Employee("John Doe", 50000)
    print(employee1.get_employee_info())

    employee1.update_salary(5000)
    print(f"Gaji setelah kenaikkan: {employee1.get_salary()}")

    employee1.set_salary(60000)
    print(f"Informasi terbaru: {employee1.get_employee_info()}")