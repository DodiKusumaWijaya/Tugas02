class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} telah ditambahkan ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pelanggan yang dapat dilayani.")
        else:
            removed_item = self.items.pop(0)
            print(f"{removed_item} telah dilayani dan dihapus dari antrian.")

    def peek(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pelanggan di depan antrian.")
        else:
            print(f"Pelanggan di depan antrian adalah: {self.items[0]}")

    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Pelanggan-pelanggan dalam antrian (dari depan ke belakang):")
            for item in self.items:
                print(item)

# Contoh penggunaan
if __name__ == "__main__":
    atm_queue = Queue()
    
    while True:
        print("\nPilih opsi:")
        print("1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan dari antrian")
        print("3. Lihat pelanggan di depan antrian")
        print("4. Lihat semua pelanggan dalam antrian")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            pelanggan = input("Masukkan nama pelanggan yang ingin ditambahkan: ")
            atm_queue.enqueue(pelanggan)
        elif pilihan == '2':
            atm_queue.dequeue()
        elif pilihan == '3':
            atm_queue.peek()
        elif pilihan == '4':
            atm_queue.display()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")