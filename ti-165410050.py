from __future__ import print_function
import os
import capnp
load_capnp = capnp.load('ti-165410142.capnp')

def writeKomplain(file):
    loaded = load_capnp.L.new_message()
    people = loaded.init('people', 1)
    
    daus=people[0]
    daus.nama  = 'Muhammad Firdaus Nurrohim';
    daus.nim  = '165410050';
    daus.mataKuliah  = 'Konsep Cloud Komputing';
    daus.nilaiYangPantas  = 'B';
    daus.alasan  = 'Karena saya sudah maksimal dalam mengerjakan soal uts maupun uas, berusaha keras untuk memahami semua materi yang diberikan, belajar bahasa python dan cap n proto untuk mengerjakan PR ini, serta ingin membahagiakan orang tua dengan tidak ada matakuliah yang mendapat nilai dibawah B';

    loaded.write(file)

def print(file):
    loaded = load_capnp.L.read(file)
 
    for data in loaded.people:
        print('Nama = ',Data.nama)
        print('Nim = ',Data.nim)
	print('Mata Kuliah = ',Data.mataKuliah)
	print('Nilai yang pantas saya dapatkan = ',Data.nilaiYangPantas)
	print('Alasan = ',Data.alasan)
 
 
if __name__ == '__main__':
    f = open('hasil', 'w')
    writeKomplain(f)
 
    f = open('hasil', 'r')
print(f)