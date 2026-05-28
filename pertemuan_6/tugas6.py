class PerangkatElektronik:
    def __init__(self, merk):
        self.merk = merk
        print(f"Menginisialisasi Perangkat Elektronik: {self.merk}")

    def info(self):
        return f"Perangkat Merk: {self.merk}"

class Kamera(PerangkatElektronik):
    def __init__(self, merk, resolusi):
        # Menggunakan super() untuk meneruskan ke PerangkatElektronik
        super().__init__(merk)
        self.resolusi = resolusi
        print(f"Menginisialisasi Fitur Kamera: {self.resolusi} MP")

    def info(self):
        return super().info() + f" | Resolusi Kamera: {self.resolusi} MP"

class Smartphone(PerangkatElektronik):
    def __init__(self, merk, os):
        # Menggunakan super() untuk meneruskan ke PerangkatElektronik
        super().__init__(merk)
        self.os = os
        print(f"Menginisialisasi Fitur Smartphone: OS {self.os}")

    def info(self):
        return super().info() + f" | Sistem Operasi: {self.os}"


class KameraSmartphone(Kamera, Smartphone):
    def __init__(self, merk, resolusi, os, nama_model):
        # super() di sini akan otomatis mengatur urutan pemanggilan berdasarkan MRO Python
        super().__init__(merk, resolusi)
        # Karena keterbatasan argumen dari multiple inheritance yang dinamis, 
        # kita pastikan atribut spesifik dari Smartphone terisi dengan baik jika belum ter-handle
        self.os = os 
        self.nama_model = nama_model
        print(f"Menginisialisasi KameraSmartphone: {self.nama_model}")

    def info(self):
        # Memanggil metode info dari parent class secara berantai lewat super()
        return super().info() + f" | Model: {self.nama_model}"


if __name__ == "__main__":
    print("--- Proses Inisialisasi Objek (Perhatikan urutan super() bekerja) ---")
    hp_baru = KameraSmartphone(merk="Samsung", resolusi=108, os="Android", nama_model="Galaxy S26")
    
    print("\n--- Output Informasi Objek ---")
    print(hp_baru.info())
    
    print("\n--- Urutan MRO (Method Resolution Order) ---")
    for urutan in KameraSmartphone.__mro__:
        print(urutan)