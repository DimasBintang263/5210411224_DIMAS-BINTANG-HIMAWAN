"""
Nama : DIMAS BINTANG HIMAWAN
NIM  : 5210411224
# 1. Kelas Menu
"""

class Menu:
  def __init__(self,nama,deskripsi,harga,rating,tipe):
    self.nama = nama
    self.deskripsi = deskripsi
    self.harga = harga
    self.rating = rating
    self.__tipe = tipe

mnm1 = Menu('jus jambu','jus jambu merah tanpa gula',8500,8,'panas/dingin')
mnm2 = Menu('jus alpukat ori','jus alpukat dengan tambahan air gula merah',15000,7,'panas/dingin')
mnm3 = Menu('jus alpukat extra susu','jus alpukat dengan campuran susu coklat dan taburan kepingan choco',15000,10,'panas/dingin')
mnm4 = Menu('red & smooth','smoothie pisang susu dengan strawberry',175000,6,'dingin')
mnm5 = Menu('kopicap','kopi murah rasa starbucks',7000,10,'panas')
mnm6 = Menu('pop ice','minuman kelas dunia',50000,9,'dingin')

pilihan_minuman = [mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print('daftar menu Healthy Fruits')
for mn in pilihan_minuman:
  t = '{} harga Rp{}, {}, tipe: {}, rating: {}' .format(mn.nama,mn.harga,mn.deskripsi,mn._Menu__tipe,mn.rating)
  print()
  print(t)

"""# 2. Kelas Mahasiswa"""

class Mahasiswa:
  def __init__(self,nama,nim,prodi,thn_masuk,alamat,umur):
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.thn_masuk = thn_masuk
    self.alamat = alamat
    self.__umur = umur 

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020,'bengkulu',19)
m2 = Mahasiswa('Dimas',2639236,'Informatika',2021,'tais',20)
m3 = Mahasiswa('Aldi',2485252,'Informatika',2021,'magelang',19)
m4 = Mahasiswa('Taher',17538175,'Hukum',2021,'madura',20)
m5 = Mahasiswa('Fahmi',23764672,'Hukum',2020,'Tais',19)
list_mahasiswa = [m1,m2,m3,m4,m5]
print(' DAFTAR MAHASISWA ')
for m in list_mahasiswa:
  teks = '{} adalah mahasiswa {} angkatan {} dengan nim {} dengan umur {} alamat {}'.format(
      m.nama,m.prodi,m.thn_masuk,m.nim,m._Mahasiswa__umur,m.alamat)
  print()
  print(teks)

"""# 3. Kelas Buku"""

class Buku: 
  def __init__(self,judul,pengarang,tahun_terbit,harga,rating):
    self.judul = judul 
    self.pengarang = pengarang
    self.tahunTerbit = tahun_terbit
    self.__harga = harga
    self.rating = rating

buku1 = Buku('Tenggelamnya Kapal Van Wijck','HAMKA',1938,50000,7)
buku2 = Buku('Berani tidak disukai','Ichiro kishimi',2019,25000,8)
buku3 = Buku('Catatan harian sang pembunuh','Kim young-ha',2013,75000,9)

daftarbuku = [buku1,buku2,buku3]
print('''Daftar Buku''')
for buku in daftarbuku:
  t = '- buku {} karangan {} diterbitkan tahun {} memiliki harga {} dengan rating {}' .format(
      buku.judul,buku.pengarang,buku.tahunTerbit,buku._Buku__harga,buku.rating)
  print()
  print(t)
