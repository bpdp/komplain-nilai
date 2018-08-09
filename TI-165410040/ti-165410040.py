
from __future__ import print_function
import os
import capnp

capnp.remove_import_hook()
capnp=capnp.load('TI-165410040.capnp')
mahasiswa=ti-nim.mahasiswa.new_message()
mahasiswa.nama='irwan prasetyo sari'
mahasiswa.nim='165410040'
mahasiswa.Matkul='Konsep Cloud Computing'
mahasiswa.Nilai='B'
mahasiswa.alasan='saya selalu datang tepat waktu dan hanya absen 1 kali, dan saya mampu mengerjakan soal uts maupun uas dengan tuntas dan selesai,dan saya juga mengerjakan soal sesuai dengan kisi kisi yang bapak berikan,dan tulisan saya cukup bisa dibaca'

print ('NAMA :'.mahasiswa.nama)
print ('NIM :'.mahasiswa.nim)
print ('MATA KULIAH :'.mahasiswa.Matkul)
print ('NILAI YANG PANTAS SAYA DAPATKAN :'.mahasiswa.Nilai)
print ('ALASAN :'.mahasiswa.alasan)