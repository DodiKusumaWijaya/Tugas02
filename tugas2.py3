from collections import deque

class ParkingLot:
    def __init__(self, capacity):
        self.lot = deque()
        self.capacity = capacity

    def is_full(self):
        return len(self.lot) == self.capacity

    def is_empty(self):
        return len(self.lot) == 0

    def park_vehicle(self, vehicle):
        if self.is_full():
            print("Parkiran penuh, kendaraan tidak dapat diparkir.")
        else:
            self.lot.append(vehicle)
            print(f"Kendaraan {vehicle} telah diparkir.")

    def remove_vehicle_front(self):
        if self.is_empty():
            print("Parkiran kosong, tidak ada kendaraan yang dapat dikeluarkan.")
        else:
            removed_vehicle = self.lot.popleft()
            print(f"Kendaraan {removed_vehicle} telah dikeluarkan dari depan parkiran.")

    def remove_vehicle_back(self):
        if self.is_empty():
            print("Parkiran kosong, tidak ada kendaraan yang dapat dikeluarkan.")
        else:
            removed_vehicle = self.lot.pop()
            print(f"Kendaraan {removed_vehicle} telah dikeluarkan dari belakang parkiran.")

    def display(self):
        if self.is_empty():
            print("Parkiran kosong.")
        else:
            print("Kendaraan dalam parkiran (dari depan ke belakang):")
            for vehicle in self.lot:
                print(vehicle)

# Simulasi pendaftaran mahasiswa untuk topik proyek
class TopicRegistration:
    def __init__(self, max_students_per_topic):
        self.topics = {
            "stack": [],
            "queue": [],
            "deque": []
        }
        self.max_students_per_topic = max_students_per_topic

    def register_student(self, student, topic):
        if topic not in self.topics:
            print("Topik tidak valid.")
            return
        
        if len(self.topics[topic]) >= self.max_students_per_topic:
            print(f"Topik {topic} sudah penuh. Mahasiswa {student} tidak dapat mendaftar.")
        else:
            self.topics[topic].append(student)
            print(f"Mahasiswa {student} telah mendaftar untuk topik {topic}.")

    def display_registrations(self):
        print("Pendaftaran mahasiswa untuk setiap topik:")
        for topic, students in self.topics.items():
            print(f"Topik {topic}: {students}")

# Contoh penggunaan
if __name__ == "__main__":
    # Simulasi parkiran kendaraan
    parkiran = ParkingLot(capacity=5)
    
    while True:
        print("\nPilih opsi parkiran:")
        print("1. Parkir kendaraan")
        print("2. Keluarkan kendaraan dari depan")
        print("3. Keluarkan kendaraan dari belakang")
        print("4. Lihat semua kendaraan dalam parkiran")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            kendaraan = input("Masukkan nama kendaraan yang ingin diparkir: ")
            parkiran.park_vehicle(kendaraan)
        elif pilihan == '2':
            parkiran.remove_vehicle_front()
        elif pilihan == '3':
            parkiran.remove_vehicle_back()
        elif pilihan == '4':
            parkiran.display()
        elif pilihan == '5':
            print("Program parkiran selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    # Simulasi pendaftaran mahasiswa untuk topik proyek
    registrasi_topik = TopicRegistration(max_students_per_topic=10)
    
    while True:
        print("\nPilih opsi pendaftaran topik:")
        print("1. Daftarkan mahasiswa untuk topik")
        print("2. Lihat pendaftaran mahasiswa")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            mahasiswa = input("Masukkan nama mahasiswa: ")
            topik = input("Masukkan topik (stack/queue/deque): ")
            registrasi_topik.register_student(mahasiswa, topik)
        elif pilihan == '2':
            registrasi_topik.display_registrations()
        elif pilihan == '3':
            print("Program pendaftaran selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")