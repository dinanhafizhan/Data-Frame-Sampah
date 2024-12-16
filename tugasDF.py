import pandas as pd
#1 DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat.
file = "D:/KULIAH DINAN/SEMESTER 3/PEMDAS/Reguler/Tugas/pandas/data_sampah.csv"
df = pd.read_csv(file)
df = df[["nama_kabupaten_kota", "tahun", "jumlah_produksi_sampah"]]
df = df.dropna()
print(df)
#2 hitung total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun 2015
jumlah_sampah_2015 = []
for i, row in df.iterrows():
    if row['tahun'] == 2015:
        jumlah_sampah_2015.append(row['jumlah_produksi_sampah'])
print(f"Jumlah sampah pada tahun 2015: {sum(jumlah_sampah_2015)}")

#3 Jumlah data pertahun
jumlah_pertahun = {} 

for i, row in df.iterrows():
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_produksi_sampah']  
    jumlah_pertahun[tahun] = jumlah_pertahun.get(tahun, 0) + jumlah_sampah
    
for tahun, total_sampah in jumlah_pertahun.items():
    print(f"Tahun {tahun}: {total_sampah}")


#4 Jumlah data perkota
jumlah_per_kota_tahun = {}
for i, row in df.iterrows():
    key = (row['nama_kabupaten_kota'], row['tahun'])
    jumlah_per_kota_tahun[key] = jumlah_per_kota_tahun.get(key, 0) + row['jumlah_produksi_sampah']

for key, total_sampah in jumlah_per_kota_tahun.items():
    print(f"Total Sampah {key[0]} Tahun {key[1]}: {total_sampah}")


hasil_df = pd.DataFrame( [(kota, tahun, total) for (kota, tahun), total in jumlah_per_kota_tahun.items()],
columns=["nama_kabupaten_kota", "tahun", "jumlah_produksi_sampah"])

hasil_df.to_csv("hasil_produksi_sampah.csv", index=False)
hasil_df.to_excel("hasil_produksi_sampah.xlsx", index=False)


