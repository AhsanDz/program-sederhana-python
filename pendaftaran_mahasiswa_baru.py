def tambah_mahasiswa(data_mahasiswa):
    print("\n--- TAMBAH MAHASISWA BARU ---")
    nim = input("Masukkan NIM: ")

    if nim in data_mahasiswa:
        print("NIM sudah terdaftar.")
        return

    if not nim :
        print("NIM tidak boleh kosong.")
        return

    nama = input("Masukkan Nama: ")
    if not nama:
        print("Nama tidak boleh kosong.")
        return

    prodi = input("Masukkan Prodi: ")
    if not prodi:
        print("Prodi tidak boleh kosong.")
        return

    ipk = float(input("Masukkan IPK: "))
    if ipk < 0.0 or ipk > 4.0:
        print("IPK harus antara 0.0 dan 4.0.")
        return

    data_mahasiswa[nim] = {
        'nama': nama,
        'prodi': prodi,
        'ipk': ipk
    }
    print(f"Mahasiswa dengan NIM {nim} berhasil ditambahkan.")

def tampilkan_mahasiswa(data_mahasiswa):
    print("\n--- DAFTAR SEMUA MAHASISWA ---")
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
        return

    print("Total Mahasiswa:", len(data_mahasiswa))
    for nim, info in data_mahasiswa.items():
        print(f"NIM: {nim}, Nama: {info['nama']}, Prodi: {info['prodi']}, IPK: {info['ipk']}")

def cari_mahasiswa(data_mahasiswa):
    print("\n--- CARI MAHASISWA ---")
    nim = input("Maukkan NIM yang dicari: ")

    if nim in data_mahasiswa:
        info = data_mahasiswa[nim]
        print(f"NIM: {nim}, Nama: {info['nama']}, Prodi: {info['prodi']}, IPK: {info['ipk']}")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

def hapus_mahasiswa(data_mahasiswa):
    print("\n--- HAPUS MAHASISWA ---")
    nim = input("Masukkan NIM yang akan dihapus: ")

    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

#
print("Program Pendaftaran Mahasiswa Baru")
print("="*35)
data_mahasiswa = {}

while True:
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_mahasiswa(data_mahasiswa)
    elif pilihan == '2':
        tampilkan_mahasiswa(data_mahasiswa)
    elif pilihan == '3':
        cari_mahasiswa(data_mahasiswa)
    elif pilihan == '4':
        hapus_mahasiswa(data_mahasiswa)
    elif pilihan == '5':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
