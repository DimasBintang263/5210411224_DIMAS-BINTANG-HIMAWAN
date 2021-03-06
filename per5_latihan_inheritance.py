"""
Nama: Dimas Bintang Himawan
Nim: 5210411224
"""
"""
# 1. Class Hewan Single
"""

#Single Inheritance

#Parent Class
class Hewan :   
    def bersuara(self) :
        print("Kucing Bersuara")

# Anak class mewarisi parent class
class Kucing(Hewan) :
    def suara(self) :
        print("miaw...miaw")

#Objek
cat = Kucing()
cat.suara()
cat.bersuara()

"""# 2. Class Hewan Multilevel"""

#Multilevel Inheritance
#Parent Class
class Hewan :
    def bersuara(self) :
        print("Kucing Bersuara")
#Anak class mewarisi class hewan
class Kucing(Hewan) :
    def suara(self) :   
        print("miaw...miaw")

#Anak class Anakkucing mewarisi dari class hewan
class AnakKucing(Kucing) :
    def minum(self) :   
        print("Minum air")
#Objek
cat = AnakKucing()
cat.bersuara()
cat.suara()
cat.minum()

"""# 3. Class Hewan Hierarchical"""

#Hierarchical Inheritance

#Parent Class
class Induk :
    def fungsiinduk(self) :
        print("Fungsi pada parent class.")
#Class turunan 1
class Anak1(Induk) :
    def fungsianak1(self) :
        print("Fungsi pada anak 1.")
#Class turunan 2
class Anak2(Induk) :
    def fungsianak2(self) :
        print("Fungsi pada anak 2.")

#Objek
child1 = Anak1()
child2 = Anak2()

child1.fungsiinduk()
child1.fungsianak1()

child2.fungsiinduk()
child2.fungsianak2()

"""# 4. Class Mahasiswa Single"""

#Single Inheritance
class Mahasiswa :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim    
    def detailMhs(self) :
        return self.nim, self.nama

    def cekMhs(self) :  
        if self.nim < 150000 :
            return "Mahasiswa Aktif"
        else :
            return "Mahasiswa Tidak Terdaftar"

class Siswa(Mahasiswa) :
    def End(self) : 
        print("Mahasiswa belum melakukan daftar ulang")
mhs1 = Mahasiswa("Mahasiswa 1", 135103)
print(mhs1.detailMhs(), mhs1.cekMhs())
mhs2 = Siswa("Mahasiswa 2", 150503)
print(mhs2.detailMhs(), mhs2.cekMhs())
mhs2.End()

"""# 5. Class Mahasiswa Multilevel"""

#Multilevel Inheritance
class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim
class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim):
        super().__init__(nama, nim)
        
class Siswa2(Siswa1) :
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim  
mahasiswa1 = Mahasiswa("Mikasa", 135105)
mahasiswa2 = Siswa1("Nezuko", 135117)
mahasiswa3 = Siswa2("Hancock", 134079)

print(mahasiswa1.nama, mahasiswa1.nim)
print(mahasiswa2.nim)   
print(mahasiswa3.nama)

"""# 6. Class Mahasiswa Hierarchial"""

#Hierarchial Inheritance
class Mahasiswa() :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim    
    def detSiswa1(self) :
        print(self.nama, "Alamat : Wall Rose")

class Siswa2(Mahasiswa) :
    def __init__(self, nama, nim) :
        self.nama = nama
        self.nim = nim  
    def detSiswa2(self) :
        print(self.nama, "Jurusan : Informatika")

mahasiswa1 = Siswa1("Mikasa", 135105)
mahasiswa2 = Siswa2("Nezuko", 135117)

print(mahasiswa1.nim)   
mahasiswa1.detSiswa1()
print(mahasiswa2.nim)
mahasiswa2.detSiswa2()

"""# 7. Class Mahasiswa Multiple"""

#Multiple Inheritance
class Mahasiswa1() :
    def __init__(self, nama, nim ) :
        self.nama = nama
        self.nim = nim
class Mahasiswa2() :
    def __init__(self, alamat, jurusan) :
        self.alamat = alamat
        self.jurusan = jurusan   
class Siswa(Mahasiswa1, Mahasiswa2) :
    def __init__(self, nama, nim, alamat, jurusan) :
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self, alamat, jurusan)

s = Siswa("Mikasa", 135105, "Wall Rose", "Informatika") 
print(f"Nim : {s.nim}, Nama : {s.nama} Alamat : {s.alamat} Jurusan : {s.jurusan}")

"""# 8. Class Perhitungan Multiple"""

#Multiple Inheritance

#Parent Class 1
class Perhitungan1 :
    def penjumlahan(self, a, b) :
        return a + b
#Parent Class 2
class Perhitungan2 :
    def perkalian(self, a, b) :
        return a * b    

#Anak Class
class Hitung(Perhitungan1, Perhitungan2) :
    def pembagian(self, a, b):
        return a / b    
#Objek
h = Hitung()    
print(h.penjumlahan(20, 20))
print(h.perkalian(5, 4))
print(h.pembagian(6, 12))

"""# 9. Class ComputerPart"""

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed) :
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas 
    
class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm  
p = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
m = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

parts = [p, m, hdd]
for part in parts :
    print('{} {} produksi {}'.format(part.jenis, part.nama, part.pabrikan))
