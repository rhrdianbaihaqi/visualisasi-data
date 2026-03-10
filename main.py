from src import modul2_sintaks, modul2_struktur, modul3_baca, modul4_visual

def main():
    print("=== MEMULAI EKSEKUSI TUGAS PYTHON ===")
    
    print("\n[1] Menjalankan Modul 2: Sintaks & Dasar")
    modul2_sintaks.run_modul()
    
    print("\n[2] Menjalankan Modul 2: Struktur Data & Logika")
    modul2_struktur.run_modul()
    
    print("\n[3] Menjalankan Modul 3: Ingestion Data")
    modul3_baca.run_modul()
    
    print("\n[4] Menjalankan Modul 4: Visualisasi Scatter Plot")
    modul4_visual.tampilkan_scatter_plot()
    
    print("\n[5] Menjalankan Latihan Modul 4: Visualisasi Pie Chart (Gender)")
    modul4_visual.tampilkan_pie_chart_gender()
    
    print("\n=== EKSEKUSI SELESAI ===")

if __name__ == '__main__':
    main()