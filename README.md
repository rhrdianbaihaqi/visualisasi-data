# Proyek Tugas Python (Machine Learning Dasar)

**Identitas Mahasiswa:**
- **Nama:** [Nama Anda / Muhammad Rahardian Baihaqi]
- **NIM:** [NIM Anda]
- **Kelas:** [Sebutkan Kelas/Grup]
- **Mata Kuliah:** [Sebutkan Mata Kuliah - misal: Machine Learning / Kecerdasan Buatan]

Proyek ini berisi kumpulan tugas pemrograman Python yang diatur ke dalam beberapa modul terpisah. Proyek ini mengimplementasikan dasar-dasar sintaks, struktur data, pembacaan data, hingga visualisasi menggunakan pustaka seperti Pandas dan Matplotlib.

## Struktur Direktori
- `main.py` -> File utama (*Orchestrator*) yang akan mengeksekusi semua modul secara berurutan.
- `src/` -> Menyimpan kode sumber (*source code*) yang sudah dipecah berdasarkan topik (Sintaks, Struktur, Ingestion, Visual).
- `data/` -> Direktori lokal yang memuat dataset yang digunakan untuk modul tugas pembacaan data pandas (contoh: `tips.csv`).
- `requirements.txt` -> Daftar dependensi *third-party* (seperti `pandas`, `matplotlib`) yang dibutuhkan.

## Cara Instalasi dan Penggunaan

1. **Persiapan Virtual Environment (Opsional namun disarankan):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Mac/Linux
   # atau `venv\Scripts\activate` untuk Windows
   ```

2. **Instalasi Pustaka (Dependensi):**
   Silakan jalankan perintah ini di terminal untuk menginstal library Python yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Menjalankan Proyek:**
   Seluruh modul akan berjalan jika Anda mengeksekusi skrip komandan utama:
   ```bash
   python main.py
   ```
   > **Catatan:** Pada modul 4 (Visualisasi), program akan menampilkan jendela diagram (seperti *Scatter Plot* atau *Pie Chart*). Program utama mungkin tertahan sampai Anda menutup jendela plot tersebut.

---
*Dibuat untuk keperluan Tugas Kuliah.*
