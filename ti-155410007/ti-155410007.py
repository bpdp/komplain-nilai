from __future__ import print_function
import os
import capnp

capnp.remove_import_hook()
khs = capnp.load('ti-155410007.capnp')


def buatFileOutput(file):
    tccl = khs.NilaiTCCL.new_message()
    mahasiswa = tccl.init('mahasiswa', 1)
 
    mhs = mahasiswa[0]
    mhs.nama = 'Dhitya Pamungkas'
    mhs.nim = '155410007'
    mhsNgimpi = mhs.init('penilaian', 1)
    mhsNgimpi[0].makul = "Teknologi Cloud Computing Lanjut [Teori & Praktikum]"
    mhsNgimpi[0].nilaiIdaman = 'A'
    mhsNgimpi[0].alasan = 'Saya sudah berusaha keras sepanjang semester untuk mengimplementasikan materi yang diajarkan. Beberapa teknologi juga saya terapkan di kantor (walau beberapa masih tahap evaluasi). Mudah-mudahan dengan usaha terahir ini bisa memperbaiki nilai mata kuliah 3 sks dan 1 praktikum :D'
 
    tccl.write(file)
 
 
def bacaFileOutput(file):
    tccl = khs.NilaiTCCL.read(file)
 
    for identitas in tccl.mahasiswa:
        print('Nama = ',identitas.nama)
        print('Nim = ',identitas.nim)
        for data in identitas.penilaian:
            print('Mata Kuliah = ',data.makul)
            print('Nilai yang pantas didapat = ',data.nilaiIdaman)
            print('Alasan = ',data.alasan)
 
 
if __name__ == '__main__':
    transkrip = open('KartuHasilStudi', 'w')
    buatFileOutput(transkrip)
 
    transkrip = open('KartuHasilStudi', 'r')
    bacaFileOutput(transkrip) 
