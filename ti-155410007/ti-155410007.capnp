@0xc119de152b72585d;

struct KHS {
    nama @0 :Text;
    nim @1 :Text;
    penilaian @2 :List(DataNilai);

    struct DataNilai {
        makul @0 :Text;
        nilaiIdaman @1 :Text;
        alasan @2 :Text;
        }
}

struct NilaiTCCL {
    mahasiswa @0 :List(KHS);
} 
