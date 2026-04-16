class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            print("Nama tidak boleh kosong.")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value<0:
            print("Umur tidak boleh negatif!")
        else:
            self.__age = value

def main():
    person = Person("Alice", 30)
    print(f"Nama: {person.name}, Umur: {person.age}")

    person.name = "Bob"
    person.age = 35
    print(f"Nama baru: {person.name}, Umur baru; {person.age}")

    person.age = -5

if __name__ == "__main__":
    main() 
