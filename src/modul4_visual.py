import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, 'data', 'tips.csv')

def get_dataframe():
    if not os.path.exists(FILE_PATH):
        print("[Error] Dataset tidak ditemukan.")
        return None
    return pd.read_csv(FILE_PATH)

def tampilkan_scatter_plot():
    df = get_dataframe()
    if df is not None:
        plt.figure(figsize=(8, 5))
        plt.scatter(df['day'], df['tip'], color='blue', alpha=0.6)
        plt.title("Scatter Plot: Day vs Tip", fontsize=14)
        plt.xlabel('Day', fontsize=12)
        plt.ylabel('Tip ($)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

def tampilkan_pie_chart_gender():
    df = get_dataframe()
    if df is not None and 'sex' in df.columns:
        gender_counts = df['sex'].value_counts()
        
        plt.figure(figsize=(7, 7))
        plt.pie(gender_counts, 
                labels=gender_counts.index, 
                autopct='%1.1f%%', 
                startangle=90, 
                colors=['#4CAF50', '#FF9800'], 
                explode=(0.05, 0), 
                shadow=True)
        plt.title("Persentase Pemberi Tip Berdasarkan Gender", fontweight='bold')
        plt.tight_layout()
        plt.show()