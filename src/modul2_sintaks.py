def math_and_string():
    greeting = 'Hello World!'
    bahasa = 'Py' 'thon'
    
    print(f"String  : {greeting} | Panjang: {len(greeting)}")
    print(f"Gabungan: {greeting + bahasa}")
    
    print(f"Bagi (Float): {17 / 3}")
    print(f"Bagi (Floor): {17 // 3}")
    print(f"Modulo      : {17 % 3}")
    
    tax = 12.5 / 100
    price = 100.50
    print(f"Harga + Pajak (Bulat): {round(price + (price * tax), 3)}")

def input_output():
    name = input('Masukan nama Anda: ').strip()
    print(f"Halo, {name}!" if name else "Input kosong.")

def run_modul():
    math_and_string()
    pass