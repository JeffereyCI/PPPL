### Implementasi Observer Design Pattern
**pada sistem pemantau suhu**

### Struktur Komponen

- **Subject:**  
  - `TemperatureSensor`  
    Menyimpan nilai suhu dan daftar observer. Saat suhu diubah melalui `set_temperature`, subject memanggil `notify_observers` untuk mengirim update ke semua observer terdaftar.
- **Observer:**  
  - `CurrentConditionsDisplay`  
    Menampilkan suhu terbaru setiap kali ada perubahan.
  - `StatisticsDisplay`  
    Menyimpan seluruh riwayat suhu yang diterima, lalu menampilkan suhu rata-rata, minimum, dan maksimum.
- **Interface:**  
  - `Observer`  
    Mendefinisikan method `update(temperature: float)` yang harus diimplementasikan oleh semua observer.
  - `Subject`  
    Mendefinisikan method `register_observer`, `remove_observer`, dan `notify_observers`.

### Alur Kerja

1. Program utama (`main.py`) membuat objek subject (`TemperatureSensor`) dan observer (`CurrentConditionsDisplay`, `StatisticsDisplay`).
2. Observer didaftarkan ke subject menggunakan `register_observer`.
3. Saat suhu diubah melalui `set_temperature`, subject memanggil `notify_observers`.
4. Setiap observer menerima update dan menampilkan informasi sesuai fungsinya.
5. Observer dapat dihapus dari subject kapan saja menggunakan `remove_observer`.

## Cara Menjalankan

1. Jalankan `main.py`.
2. Masukkan suhu baru sesuai instruksi untuk melihat notifikasi ke observer.
3. Observer dapat ditambah atau dihapus dari subject sesuai kebutuhan (dapat dikembangkan lebih lanjut).
