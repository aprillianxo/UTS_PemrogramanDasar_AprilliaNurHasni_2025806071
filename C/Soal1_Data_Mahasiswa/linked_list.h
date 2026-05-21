#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Mahasiswa {
    char nama[100];
    char nim[20];
    float tugas, uts, uas;
    float nilaiAkhir;
    char mutu;
    struct Mahasiswa *next;
} Mhs;

// Function Prototype
float hitungNilaiAkhir(float tugas, float uts, float uas);
char hitungMutu(float nilai);

void tambahMahasiswa(Mhs **head);
void tampilkanMahasiswa(Mhs *head);
void cariMahasiswa(Mhs *head);
void hapusMahasiswa(Mhs **head);
void simpanCSV(Mhs *head);
void freeMemory(Mhs *head);

#endif