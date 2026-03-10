def manipulasi_koleksi():
    contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
    print(f"List Asli (Len {len(contoh_list)}): {contoh_list}")
    
    contoh_set = set(contoh_list)
    print(f"Set Unik  (Len {len(contoh_set)}): {contoh_set}")
    
    angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
    print(f"Min: {min(angka)}, Max: {max(angka)}")
    
    kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
    kendaraan.sort(reverse=True)
    print(f"Kendaraan Descending: {kendaraan}")

def efisiensi_looping():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(f"Kata: {w}, Panjang: {len(w)}")

    users = {'Hans': 'active', 'Eleonore': 'inactive', 'Keitaro': 'active'}
    active_users = {user: status for user, status in users.items() if status == 'active'}
    print(f"Active Users (Optimized): {active_users}")

def control_statement():
    x = 42
    if x < 0:
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

def run_modul():
    manipulasi_koleksi()
    efisiensi_looping()
    control_statement()