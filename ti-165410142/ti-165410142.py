from __future__ import print_function
import os
import capnp

capnp.remove_import_hook()
kcc_capnp = capnp.load('ti-165410142.capnp')


def writeKcc(file):
    kcc = kcc_capnp.Kcc.new_message()
    people = kcc.init('people', 1)
 
    bilal = people[0]
    bilal.nama = 'Muhammad Bilal Shah'
    bilal.nim = '165410142'
    bilalKomplain = bilal.init('komplain', 1)
    bilalKomplain[0].mataKuliah = "Konsep Cloud Computing"
    bilalKomplain[0].nilaiPantas = 'B'
    bilalKomplain[0].alasan = 'Saya rajin berangkat, presensi saya baik, d atas 80%, selalu mengikuti kuliah dari awal sampai akhir, mendengarkan dengan baik kuliah bapak, dan beberapa teman yang sama seperti saya juga mendapatkan nilai B walau tidak maju presentasi ke depan.'

 
    kcc.write(file)
 
 
def printKcc(file):
    kcc = kcc_capnp.Kcc.read(file)
 
    for mahasiswa in kcc.people:
        print('Nama = ',mahasiswa.nama)
        print('Nim = ',mahasiswa.nim)
        for komplain in mahasiswa.komplain:
	        print('Mata Kuliah = ',komplain.mataKuliah)
	        print('Nilai yang pantas saya dapatkan = ',komplain.nilaiPantas)
	        print('Alasan = ',komplain.alasan)
 
 
if __name__ == '__main__':
    f = open('hasil', 'w')
    writeKcc(f)
 
    f = open('hasil', 'r')
    printKcc(f)