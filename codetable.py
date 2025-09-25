import json
import csv
from datetime import datetime

# --- BACA FILE JSON ---
file_path = "Kharindra Argiansya_V3925027.json"  # ganti sesuai lokasi file JSON
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- FUNGSI FORMAT TANGGAL ---
def format_tanggal(tanggal_str):
    try:
        return datetime.strptime(tanggal_str, "%Y-%m-%d").strftime("%d-%m-%Y")
    except:
        return tanggal_str

# --- FUNGSI UNTUK SIMPAN LIST DICTIONARY KE CSV ---
def simpan_csv(nama_file, data_list, fieldnames):
    with open(nama_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)
    print(f"✅ Data berhasil disimpan ke {nama_file}")

# ===================================================
# 1. INTEGRASI RESMI
integrasi_data = []
for item in data["integrasi_Resmi"]:
    integrasi_data.append({
        "id_integrasi": item["id_integrasi"],
        "tanggal": format_tanggal(item["tanggal"]),
        "lokasi": item["lokasi"],
        "lat": item["koordinat"]["lat"],
        "lon": item["koordinat"]["lon"],
        "tingkat": item["tingkat"],
        "status": item["status"]
    })

simpan_csv("integrasi_resmi.csv", integrasi_data,
           ["id_integrasi", "tanggal", "lokasi", "lat", "lon", "tingkat", "status"])

# ===================================================
# 2. LAPORAN MASYARAKAT
laporan_data = []
for item in data["laporan_masyarakat"]:
    laporan_data.append({
        "id_laporan": item["id_laporan"],
        "tanggal": format_tanggal(item["tanggal"]),
        "pelapor": item["pelapor"],
        "lokasi": item["lokasi"],
        "deskripsi": item["deskripsi"],
        "status": item["status"]
    })

simpan_csv("laporan_masyarakat.csv", laporan_data,
           ["id_laporan", "tanggal", "pelapor", "lokasi", "deskripsi", "status"])

# ===================================================
# 3. MEDIA SOSIAL
media_data = []
for item in data["media_sosial"]:
    media_data.append({
        "id_media": item["id_media"],
        "tanggal": format_tanggal(item["tanggal"]),
        "platform": item["platform"],
        "keyword": item["keyword"],
        "status": item["status"]
    })

simpan_csv("media_sosial.csv", media_data,
           ["id_media", "tanggal", "platform", "keyword", "status"])

# ===================================================
# 4. SENSOR IoT CCTV
sensor_data = []
for item in data["sensor_IoT_cctv"]:
    sensor_data.append({
        "id_sensor": item["id_sensor"],
        "tanggal": format_tanggal(item["tanggal"]),
        "lokasi": item["lokasi"],
        "lat": item["koordinat"]["lat"],
        "lon": item["koordinat"]["lon"],
        "sensor": item["sensor"],
        "deteksi": item["deteksi"]
    })

simpan_csv("sensor_iot_cctv.csv", sensor_data,
           ["id_sensor", "tanggal", "lokasi", "lat", "lon", "sensor", "deteksi"])
