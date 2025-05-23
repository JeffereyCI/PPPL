### Implementasi Command Design Pattern
**pada aplikasi todo list sederhana**

### Struktur Komponen

- **Command (Interface):**  
  - `Command`  
    Mendefinisikan method `execute()` dan `undo()` yang harus diimplementasikan oleh semua perintah.

- **Concrete Command:**  
  - `AddTaskCommand`  
    Menambah tugas ke todo list.
  - `RemoveTaskCommand`  
    Menghapus tugas dari todo list.
  - `MarkAsDoneCommand`  
    Menandai tugas sebagai selesai.

- **Receiver:**  
  - `TodoList`  
    Menyimpan daftar tugas dan menyediakan operasi untuk menambah, menghapus, dan menandai tugas.

- **Invoker:**  
  - `CommandManager`  
    Menangani eksekusi command, menyimpan history untuk mendukung fitur undo dan redo.

### Alur Kerja

1. Program utama (`main.py`) membuat objek `TodoList` dan `CommandManager`.
2. Pengguna memilih operasi (tambah, hapus, tandai selesai).
3. Command yang sesuai dibuat dan dieksekusi melalui `CommandManager`.
4. Setiap command yang dieksekusi disimpan dalam history untuk mendukung undo dan redo.
5. Pengguna dapat melakukan undo/redo beberapa langkah sesuai kebutuhan.

## Cara Menjalankan

1. Jalankan `main.py`.
2. Pilih operasi yang diinginkan (Add Task, Remove Task, Mark as Done, History, Undo, Redo, Exit).
3. Lihat perubahan pada daftar tugas dan history command.
4. Gunakan fitur undo/redo untuk membatalkan atau mengulangi operasi.

---

### Kriteria Penilaian

- Implementasi Command Pattern yang benar.
- Kemampuan melakukan undo/redo beberapa langkah.
- Kejelasan dan kualitas kode.
