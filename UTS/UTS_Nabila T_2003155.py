#informasi saldo, tambah saldo, ambil saldo, keluar aplikasi.
#penyimpanan saldo: Saldo umum, saldo tabungan

saldo = 5670000
pin = 2003155

def cek_saldo():
    print ('Saldo anda sebesar RP {}'.format(saldo))

def setor_tunai(jumlah_setor_tunai):

    global saldo
    global pil
    global saldo_umum
    print ('Pilih jenis saldo:')
    print ('1. Umum')
    print ('2. Tabungan')
    if pil == 1:
        saldo_umum = saldo_umum + jumlah_setor_tunai
        print('Anda memiliki saldo umum sejumlah Rp'.format(saldo))
    elif pil == 2:
        saldo = saldo + jumlah_setor_tunai
        print ("Saldo tabungan anda sekarang Rp {}".format(saldo))

def tarik_tunai(jumlah_tarik_tunai):
    global saldo
    print ('Saldo anda Rp {}'.format(saldo))
    saldo = saldo - jumlah_tarik_tunai
    print ("Saldo anda sekarang Rp {}".format(saldo))

#antarmuka command line interface

pilihan = None
jumlah = None
while True == "y":
    print ("""" ****
    Selamat datang di BANK CERIA
            1. Cek Saldo
            2. Setor Tunai 
            3. Tarik Tunai
            4. Keluar
            **** """"")
pilihan = int(input("Silakan masukkan pilihan: "))
if pilihan == 1:
    cek_saldo
elif pilihan == 2:
    jumlah = int (input("Masukkan jumlah setor tunai: "))
    setor_tunai(jumlah)
elif pilihan == 3:
    jumlah = int (input("Masukkan jumlah tarik tunai:"))
    tarik_tunai(jumlah)
elif pilihan == 4:
    print("""Anda ingin membatalkan transaski?
        1. Iya
        2. Tidak
    """)
else:
    print ("Pilihan salah. Silakan coba lagi!")

pil = int(input("Silakan masukkan pilihan: "))
if pilihan == 1 :
    loop = "y"
else:
    print("Terimakasih telah menggunakan jasa layanan kami")