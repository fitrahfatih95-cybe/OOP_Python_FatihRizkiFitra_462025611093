class DompetDigital:
    def __init__(self, pemilik, id_pengguna, pin_awal):
        # Public Attribute
        self.pemilik = pemilik
        
        # --- PRIVATE ATTRIBUTES (Menggunakan __) ---
        self.__id_pengguna = id_pengguna
        self.__pin = pin_awal
        self.__saldo = 0  # Saldo awal 0

    # --- METODE GETTER (Akses Aman) ---
    def get_id_pengguna(self):
        "Mengambil ID Pengguna tanpa verifikasi (data identitas)."
        return self.__id_pengguna

    def get_saldo_terproteksi(self, input_pin):
        "Metode Getter untuk saldo yang memerlukan validasi PIN."
        if self.__verifikasi_pin(input_pin):
            return f"Saldo Anda saat ini: Rp{self.__saldo:,}"
        else:
            return "Akses Ditolak: PIN Salah!"

    # --- METODE VALIDASI & MODIFIKASI ---
    def __verifikasi_pin(self, input_pin):
        "Private Method untuk memvalidasi PIN (Internal saja)."
        return input_pin == self.__pin

    def tambah_saldo(self, jumlah):
        "Menambah saldo (Public method karena biasanya top-up lebih terbuka)."
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil menambah saldo sebesar Rp{jumlah:,}")
        else:
            print("Jumlah top-up harus lebih dari 0.")

    def tarik_tunai(self, jumlah, input_pin):
        "Metode modifikasi data rahasia dengan validasi ketat."
        if self.__verifikasi_pin(input_pin):
            if self.__saldo >= jumlah:
                self.__saldo -= jumlah
                print(f"Tarik tunai Rp{jumlah:,} Berhasil!")
                print(f"Sisa saldo: Rp{self.__saldo:,}")
            else:
                print("Transaksi Gagal: Saldo tidak mencukupi.")
        else:
            print("Transaksi Gagal: PIN yang Anda masukkan salah!")

# --- INSTANSIASI DAN PENGUJIAN ---

# 1. Membuat Object
dompet_chelsyi = DompetDigital("Chelsyi Danova", "USER-2026", "080706")

print(f"=== Selamat Datang, {dompet_chelsyi.pemilik} ===")

# 2. Pembuktian Encapsulation (Akses Langsung)
# Baris di bawah ini jika diaktifkan akan menyebabkan AttributeError
# print(dompet_chelsyi.__saldo) 
# print(dompet_chelsyi.__pin)
print("[INFO] Atribut privat tidak bisa diakses langsung dari luar class.")

print("-" * 40)

# 3. Pengujian Validasi (PIN Salah)
print("Mencoba cek saldo dengan PIN asal (000000):")
print(dompet_chelsyi.get_saldo_terproteksi("000000"))

print("\n")

# 4. Pengujian Validasi (PIN Benar)
dompet_chelsyi.tambah_saldo(500000) # Top up dulu
print("Mencoba tarik tunai dengan PIN benar (080706")
dompet_chelsyi.tarik_tunai(200000, "080706")

print("-" * 40)
# Tampilkan ID Pengguna melalui Getter
print(f"ID Pengguna Anda: {dompet_chelsyi.get_id_pengguna()}")