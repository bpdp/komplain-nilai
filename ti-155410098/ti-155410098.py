from __future__ import print_function
import os
import capnp
capnp.remove_import_hook()
tccl_capnp = capnp.load('ti-155410098.capnp')

def getTccl(file):
    tccl = tccl_capnp.Data.new_message()
    rows = tccl.init('tccl', 1)
 
    data        = rows[0]
    data.id     = 465
    data.nama   = 'Arif Riyadi'
    data.nim    = '155410098'
    data.makul  = 'TEKNOLOGI CLOUD COMPUTING LANJUT'
    data.nilai  = 'A'
    data.alasan = 'Presensi baik, mengikuti perkuliahan dan mengerjakan semua tugas, melengkapi semua tugas pada repsitori git, dapat mengerjakan UTS dan UAS sesuai dengan kisi-kisi yang diberikan'

    tccl.write(file)
 
def printTccl(file):
    data = tccl_capnp.Data.read(file)
 
    for mhs in data.tccl:
        print('Nama = ',mhs.nama)
        print('NIM = ',mhs.nim)
	print('Mata Kuliah = ',mhs.makul)
	print('Nilai yang pantas saya dapatkan = ',mhs.nilai)
	print('Alasan = ',mhs.alasan)
 
 
if __name__ == '__main__':
    f = open('result', 'w')
    getTccl(f)

    f = open('result', 'r')
    printTccl(f)
