class SimpleExample:
    def __init__(self, name):
        self.name = name
        print(f"Konstruktor: Objek '{self.name}' telah dibuat.")

    def __del__(self):
        print(f"Destruktor: Objek '{self.name}' sedang dihapus.")

def main():
    print("Program dimulai.\n")

    obj = SimpleExample("Demo")
    print("Program sedang berjalan...\n")

    del obj
    print("Objek telah dihapus secara eksplisit.\n")

    print("Program Selesai.")

if __name__ == "__main__":
    main()