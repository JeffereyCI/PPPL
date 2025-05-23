### Implementasi Strategy Design Pattern
**pada aplikasi kalkulator sederhana**

### Struktur Komponen

- **Strategy (Interface):**  
  - `OperationStrategy`  
    Mendefinisikan method `execute(a: int, b: int)` yang harus diimplementasikan oleh semua strategi operasi matematika.

- **Concrete Strategy:**  
  - `AddOperation`  
    Mengimplementasikan operasi penjumlahan.
  - `SubtractOperation`  
    Mengimplementasikan operasi pengurangan.
  - `MultiplyOperation`  
    Mengimplementasikan operasi perkalian.
  - `DivideOperation`  
    Mengimplementasikan operasi pembagian.

- **Context:**  
  - `Calculator`  
    Menyimpan referensi ke strategi yang digunakan. Dapat mengubah strategi operasi matematika secara dinamis melalui method `set_strategy`.

### Alur Kerja

1. Program utama (`main.py`) membuat objek `Calculator` dan strategi-strategi operasi matematika (`AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`).
2. Pengguna memilih jenis operasi yang diinginkan.
3. `Calculator` mengatur strategi yang sesuai menggunakan `set_strategy`.
4. Pengguna memasukkan nilai-nilai yang akan dihitung.
5. `Calculator` memanggil strategi yang dipilih untuk mengeksekusi operasi matematika dan menampilkan hasilnya.
6. Pengguna dapat mengganti strategi operasi kapan saja sesuai kebutuhan.

## Cara Menjalankan

1. Jalankan `main.py`.
2. Pilih operasi matematika yang diinginkan (Add, Subtract, Multiply, Divide).
3. Masukkan nilai-nilai yang akan dihitung sesuai instruksi.
4. Hasil perhitungan akan ditampilkan.
5. Ulangi proses untuk operasi lain atau keluar dari aplikasi.

---

### Kriteria Penilaian

- Implementasi Strategy Pattern yang benar.
- Pemisahan logika operasi matematis dari kelas utama (`Calculator`).
- Naming convention yang konsisten dan jelas.
