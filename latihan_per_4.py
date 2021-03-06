"""
Nama : DIMAS BINTANG HIMAWAN
NIM  : 5210411224

# 1. class segitiga
"""

class segitiga:
  def __init__(self,alas,tinggi):
    self.alas = alas
    self.tinggi = tinggi
    self.luas = 0.5 * alas * tinggi

segitiga_besar = segitiga(100,80)
print("alas: ",segitiga_besar.alas)
print("tinggi:",segitiga_besar.tinggi)
print("luas: ",segitiga_besar.luas)

"""# 2. class utama"""

class utama:
  def __init__(self):
    self._a = 2
class turunan(utama):
  def __init__(self):
    utama.__init__(self)
    print("memanggil variable protected pada class utama: ",self._a)
    self._a = 3
    print("memanggil variable protected yang dimodifikasi diluar class: ",self._a)
objek1 = turunan()
objek2 = utama()
print("memanggil variable protected dari objek1: ", objek1._a)
print("memanggil variable protected dari objek2: ", objek2._a)

"""# 3. class hitung"""

class Hitung:
  def __init__(self):
    self. __angkaRahasia = 0
  def tampilkanHitung(self):
    self. __angkaRahasia += 1
    print (self. __angkaRahasia)
hitungan=Hitung()
hitungan.tampilkanHitung()

hitungan.tampilkanHitung()

hitungan._Hitung__angkaRahasia

"""# 4. class mobil (public)"""

#variabel bersifat public
class Mobil():
  def __init__(self,jendela,pintu,mesin):
    self.jendela=jendela
    self.pintu=pintu
    self.mesin=mesin

"""# 5. class mobil(protected)"""

#variabel bersifat protected
class Mobil():
  def __init__(self,jendela,pintu,mesin):
    self._jendela=jendela
    self._pintu=pintu
    self._mesin=mesin

class Truk(Mobil):
  def __init__(self,jendela,pintu,mesin,tipe):
    super().__init__(jendela,pintu,mesin)
    self.tipebak=tipe

"""# 6. class mobil(private)"""

#variabel bersifat private
class Mobil():
  def __init__(self,jendela,pintu,mesin):
    self.__jendela=jendela
    self.__pintu=pintu
    self.__mesin=mesin

audi=Mobil(4,5,"diesel")
audi._Mobil__mesin

"""# 7. class pegawai"""

class Pegawai:
  __nama=""
  __alamat=""
  __gaji=0
  def __init__(self,nama,alamat):
    self.__nama=nama
    self.__alamat=alamat
  def __hitungGaji(self):
    upahLembur=20000
    gajiPokok=3000000
    jumLembur=int(input("Total jam lembur: "))
    self.__gaji=(upahLembur*jumLembur)+gajiPokok
  def tampilDetail(self):
    print("\n--Menghitung dan Menampilkan Detail Gaji Pegawai--")
    print("nama: ", self.__nama)
    print("alamat: ", self.__alamat)
    self.__hitungGaji()
    print("total gaji: ", self.__gaji)
pgw1=Pegawai("Eren yaeger","nganjuk")
pgw1.tampilDetail()
pgw2=Pegawai("Rias gremaory","bandung")
pgw2.tampilDetail()
