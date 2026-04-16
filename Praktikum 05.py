class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value
        print(f"Kalkulator diinisialisasi dengan nilai: {self.value}")

    def add(self, number):
        self.value += number
        print(f"Setelah penambahan {number}, nilai sekarang adalah: {self.value}")

    def substract(self, number):
        self.value -= number
        print(f"Setlah pengurangan {number}, nilai sekarang adalah: {self.value}")

    def reset(self):
        self.value = 0
        print("Nilai telah direset ke o.")
    
    def show_value(self):
        print(f"Nilai saat ini adalah: {self.value}")

def main():
    calc1 = Calculator(initial_value=10)
    calc1.add(5)
    calc1.substract(3)
    calc1.show_value()

    calc2 = Calculator()
    calc2.add(20)
    calc2.show_value()

if __name__ == "__main__":
    main()