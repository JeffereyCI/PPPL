# UTS Pemrograman Berorientasi Objek (PPPL)

Folder ini berisi tiga studi kasus implementasi design pattern menggunakan Python:

1. **Strategy Pattern**  
   Studi kasus: Kalkulator sederhana  
   Lokasi: `calculator/`

2. **Command Pattern**  
   Studi kasus: Todo List  
   Lokasi: `todo_cli/`

3. **Observer Pattern**  
   Studi kasus: Sistem Pemantau Suhu  
   Lokasi: `sistem_pemantau_suhu/`

---

## 1. Calculator (Strategy Pattern)

Aplikasi kalkulator sederhana yang dapat melakukan operasi matematika dasar (penjumlahan, pengurangan, perkalian, pembagian) menggunakan Strategy Pattern.

- **Komponen utama:**  
  - `OperationStrategy` (interface)  
  - Concrete strategy: `AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`  
  - `Calculator` (context)

- **Fitur:**  
  - Operasi matematika dapat dipilih/diganti secara dinamis.
  - Logika operasi terpisah dari kelas utama.

- **Jalankan:**  
  ```
  cd calculator
  python main.py
  ```

Penjelasan detail: lihat [`calculator/readme.md`](./calculator/readme.md)

---

## 2. Todo List (Command Pattern)

Aplikasi todo list sederhana yang mendukung operasi tambah, hapus, dan tandai selesai menggunakan Command Pattern.

- **Komponen utama:**  
  - `Command` (interface)  
  - Concrete command: `AddTaskCommand`, `RemoveTaskCommand`, `MarkAsDoneCommand`  
  - `TodoList` (receiver)  
  - `CommandManager` (invoker)

- **Fitur:**  
  - Mendukung undo/redo beberapa langkah.
  - History command dapat dilihat.

- **Jalankan:**  
  ```
  cd todo_cli
  python main.py
  ```

Penjelasan detail: lihat [`todo_cli/readme.md`](./todo_cli/readme.md)

---

## 3. Sistem Pemantau Suhu (Observer Pattern)

Aplikasi pemantau suhu yang mengimplementasikan Observer Pattern untuk notifikasi perubahan suhu.

- **Komponen utama:**  
  - `Subject` dan `Observer` (interface)  
  - `TemperatureSensor` (subject)  
  - `CurrentConditionsDisplay`, `StatisticsDisplay` (observer)

- **Fitur:**  
  - Observer dapat menerima update otomatis saat suhu berubah.
  - Statistik suhu (rata-rata, min, max) ditampilkan.

- **Jalankan:**  
  ```
  cd sistem_pemantau_suhu
  python main.py
  ```

Penjelasan detail: lihat [`sistem_pemantau_suhu/readme.md`](./sistem_pemantau_suhu/readme.md)