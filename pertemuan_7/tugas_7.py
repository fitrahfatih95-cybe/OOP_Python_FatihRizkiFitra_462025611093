class AlatPembayaran:

    """Parent Class yang mendefinisikan cetak biru (blueprint) pembayaran."""
    def __init__(self, nominal):
        self.nominal = nominal

    def proses_bayar(self):
        """Metode default yang nantinya akan di-override oleh child class."""
        print #f"Memproses pembayaran umum sebesar Rp{self.nominal:,}"


class KartuKredit(AlatPembayaran):
    """Child Class 1 yang menerapkan Method Overriding."""
    def __init__(self, nominal, nomor_kartu):
        super().__init__(nominal)
        self.nomor_kartu = nomor_kartu

    def proses_bayar(self):
        # Overriding: Logika khusus untuk pembayaran menggunakan Kartu Kredit
        sensor_kartu = f"XXXX-XXXX-XXXX-{self.nomor_kartu[-4:]}"
        print(f"[KARTU KREDIT] Memproses pembayaran sebesar Rp{self.nominal:,}")
        print(f" -> Otorisasi kartu {sensor_kartu} berhasil. Biaya admin 2% dikenakan.")
        print("-" * 50)


class EWallet(AlatPembayaran):
    """Child Class 2 yang menerapkan Method Overriding."""
    def __init__(self, nominal, nomor_hp):
        super().__init__(nominal)
        self.nomor_hp = nomor_hp

    def proses_bayar(self):
        # Overriding: Logika khusus untuk pembayaran menggunakan E-Wallet
        print(f"[E-WALLET] Memproses pembayaran sebesar Rp{self.nominal:,}")
        print(f" -> Menghubungkan ke nomor e-wallet: {self.nomor_hp}")
        print(" -> OTP Terverifikasi. Saldo berhasil dipotong.")
        print("-" * 50)


# --------------------------------------------------
# 2. BAGIAN: DUCK TYPING (Dynamic Typing khas Python)
# --------------------------------------------------

class QRPay:
    """
    Class Mandiri (Bukan bagian dari hierarki AlatPembayaran).
    Namun, kelas ini memiliki metode 'proses_bayar()'.
    Ini digunakan untuk membuktikan prinsip Duck Typing.
    """
    def __init__(self, nominal, merchant_id):
        self.nominal = nominal
        self.merchant_id = merchant_id

    def proses_bayar(self):
        # Metode dengan nama yang sama, tetapi dari kelas yang sama sekali berbeda
        print(f"[QRIS PAY] Memproses pembayaran sebesar Rp{self.nominal:,}")
        print(f" -> Memindai QR Code Merchant ID: {self.merchant_id}")
        print(" -> Pembayaran via QRIS Sukses.")
        print("-" * 50)


def jalankan_transaksi(objek_pembayaran):
    """
    Fungsi mandiri di luar kelas.
    Fungsi ini tidak peduli apa tipe data atau kelas dari objek yang masuk,
    asalkan objek tersebut memiliki metode bernama 'proses_bayar()'.
    "Jika ia berjalan seperti bebek dan bersuara seperti bebek, maka ia adalah bebek."
    """
    print(f"Menerima objek transaksi dari tipe: {type(objek_pembayaran).__name__}")
    # Memanggil metode tanpa memeriksa tipe kelas secara kaku
    objek_pembayaran.proses_bayar()


# ------------------------------------------------------------------------------
# 3. BAGIAN: DEMONSTRASI PROGRAM
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRASI POLYMORPHISM & DUCK TYPING")
    print("=" * 60)

    # Membuat instansiasi dari masing-masing class
    transaksi_kartu = KartuKredit(nominal=500000, nomor_kartu="4563123487659012")
    transaksi_wallet = EWallet(nominal=150000, nomor_hp="081234567890")
    transaksi_qris = QRPay(nominal=75000, merchant_id="MERCHANT-NURUSSALAM-01")

    # Memasukkan semua objek ke dalam list untuk dieksekusi secara polimorfis
    daftar_transaksi = [transaksi_kartu, transaksi_wallet, transaksi_qris]

    # Eksekusi fungsi menggunakan looping
    for transaksi in daftar_transaksi:
        jalankan_transaksi(transaksi)