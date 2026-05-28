class Produk:
    def __init__(self, nama, harga):
        "Inisialisasi atribut objek."
        self.nama = nama
        self.harga = harga

    def __str__(self):
        "Representasi teks saat objek di-print."
        return f"Produk: {self.nama} | Harga: Rp{self.harga:,}"

    # --- METODE PERBANDINGAN ---

    def __eq__(self, other):
        "Cek apakah harga kedua produk sama (==)."
        if isinstance(other, Produk):
            return self.harga == other.harga
        return False

    def __lt__(self, other):
        "Cek apakah harga produk ini lebih kecil dari yang lain (<)."
        if isinstance(other, Produk):
            return self.harga < other.harga
        return NotImplemented

    def __gt__(self, other):
        "Cek apakah harga produk ini lebih besar dari yang lain (>)."
        if isinstance(other, Produk):
            return self.harga > other.harga
        return NotImplemented

# --- INSTANSIASI DAN PENGUJIAN ---

# 1. Membuat 3 Object dengan data berbeda
p1 = Produk("Keyboard Mechanical", 500000)
p2 = Produk("Mouse Gaming", 350000)
p3 = Produk("Headset Wireless", 500000)

print("=== DAFTAR PRODUK (Uji __str__) ===")
print(p1)
print(p2)
print(p3)
print("-" * 40)

print("=== PENGUJIAN PERBANDINGAN ===")

# Uji __gt__ (Lebih Besar Dari)
print(f"Apakah {p1.nama} lebih mahal dari {p2.nama}? {p1 > p2}")

# Uji __lt__ (Lebih Kecil Dari)
print(f"Apakah {p2.nama} lebih murah dari {p1.nama}? {p2 < p1}")

# Uji __eq__ (Sama Dengan)
print(f"Apakah harga {p1.nama} sama dengan {p3.nama}? {p1 == p3}")
print(f"Apakah harga {p1.nama} sama dengan {p2.nama}? {p1 == p2}")