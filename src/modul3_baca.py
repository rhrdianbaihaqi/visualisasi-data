import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'tips.csv')

def baca_native_aman():
    if not os.path.exists(FILE_PATH):
        print(f"[Error] File tidak ditemukan: {FILE_PATH}")
        return

    print("--- Native File Read ---")
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        header = file.readline().strip()
        print(f"Header: {header}")
        print(f"Baris 1: {file.readline().strip()}")

def baca_pandas():
    if not os.path.exists(FILE_PATH):
        return
        
    print("\n--- Pandas Read ---")
    data = pd.read_csv(FILE_PATH)
    print(data.head(3))

def run_modul():
    baca_native_aman()
    baca_pandas()