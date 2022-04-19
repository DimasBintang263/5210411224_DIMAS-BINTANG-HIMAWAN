"""
Nama: Dimas Bintang Himawan
Nim : 5210411224
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpusdb"
)
cur=mydb.cursor()

def tambah():
    while True:
        print("1. Buku\n2. Majalah\n3. DVD\n0. Menu Utama")
        pilih = input("-->Masukan pilihan\n")
        if pilih == '1':
            id = input("-->Masukan ID\n")
            subjek = input("-->Tipe\n")
            judul = input("-->Masukan Judul\n")
            pengarang = input("-->Masukan Pengarang\n")
            cur.execute("INSERT INTO buku(id, subjek, judul, pengarang) VALUES (%s,%s,%s,%s)",(id,subjek,judul,pengarang))
            mydb.commit()
        elif pilih == '2':
            id = input("-->Masukan ID\n")
            judul = input("-->Masukan Judul\n")
            vol = input("-->Masukan Vol Majalah\n")
            issue = input("-->Masukan Issue\n")
            cur.execute("INSERT INTO majalah(id, judul, vol, issue) VALUES (%s,%s,%s,%s)",(id,judul,vol,issue))
            mydb.commit()
        elif pilih == '3':
            id = input("-->Masukan ID\n")
            judul = input("-->Masukan Judul\n")
            info = input("-->Masukan Info\n")
            cur.execute("INSERT INTO dvd(id, judul, info) VALUES (%s,%s,%s)",(id,judul,info))
            mydb.commit()
        elif pilih == '0':
            break
        else:
            print("Eror")

def tampilkan():
    cur.execute("select * from buku")
    db = cur.fetchall()
    print("\nBuku")
    for row in db:
        print(row)

    cur.execute("select * from majalah")
    print("\nMajalah")
    db = cur.fetchall()
    for row in db:
        print(row)

    cur.execute("select * from dvd")
    print("\nDVD")
    db = cur.fetchall()
    for row in db:
        print(row)

def cari():
    while True:
        print("\n1. Buku\n2. Majalah\n3. DVD\n0. Menu Utama")
        pilih= input("-->Masukan pilihan\n")
        if pilih == '1':
            id = input("-->Masukan ID\n")
            cur.execute("SELECT * FROM buku WHERE id=%s",(id,))
            p = cur.fetchall()
            print(p)
        elif pilih == '2':
            id = input("-->Masukan id yang dicari\n")
            cur.execute("SELECT * FROM majalah WHERE id=%s",(id,))
            p = cur.fetchall()
            print(p)
        elif pilih == '3':
            id = input("-->Masukan id yang dicari\n")
            cur.execute("SELECT * FROM dvd WHERE id=%s",(id,))
            p = cur.fetchall()
            print(p)
        elif pilih == '0':
            break
        else:
            print("Eror!")
print('========',"Perpustakaan",'========')
while True:
        print("\nMenu Utama")
        print("1. Tambah")
        print("2. Tampilkan")
        print("3. Cari Buku")
        print("0. Keluar")
        pilihan = input("\n-->Masukan Pilihan : ")
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            cari()
        elif pilihan == '0':
            print("\nTerimakasih ^^\n")
            break
        else:
            print("Eror!")
