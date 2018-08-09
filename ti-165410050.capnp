@0xcf2422912dfdb6b6;

struct Data{
    nama @0 : Text;
    nim @1 :Text;
    mataKuliah @2 :Text;
    nilaiYangPantas @3 :Text;
    alasan @4 :Text;
}
struct L{
    people @0 :List(Data);
}