class FileLogger:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.file = open(filename, "a")
            print(f"Gagal membuka file '{filename}': {e}")
        except Exception as e:
            print(f"Gagal membuka file '{filename}': {e}")

    def write_log(self, message):
        self.file.write(message + "\n")
        self.file.flush()
        print(f"Pesan log: '{message} telah ditulis.'")

    def __del__(self):
        if hasattr(self, "file") and not self.file.closed:
            self.file.close()
            print(f"File '{self.filename}' telah ditutup.")

if __name__ == "__main__":
    logger = FileLogger("application.log")
    logger.write_log("Aplikasi dimulai.")
    logger.write_log("Melakukan operasi A...")
    logger.write_log("Operasi A selesai.")
    logger.write_log("Aplikasi akan segera selesai.")

    del logger