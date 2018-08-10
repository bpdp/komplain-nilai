@0x934efea7f017fff0;

const qux :UInt32 = 123;

struct Mahasiswa {
    id @0 :UInt32;
    nama @1 :Text;
    nim @2 :Text;
    komplain @3 :List(KomplainNilai);

    struct KomplainNilai {
        mataKuliah @0 :Text;
        nilaiPantas @1 :Text;
        alasan @2 :Text;
        
        }
}

struct Kcc {
    people @0 :List(Mahasiswa);
}