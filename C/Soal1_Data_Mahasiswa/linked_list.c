#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "linked_list.h"

// Hitung nilai akhir
float hitungNilaiAkhir(float tugas, float uts, float uas) {
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas);
}

// Hitung huruf mutu
char hitungMutu(float nilai) {
    if (nilai >= 85)
        return 'A';
    else if (nilai >= 70)
        return 'B';
    else if (nilai >= 55)
        return 'C';
    else if (nilai >= 40)
        return 'D';
    else
        return 'E';
}

// Tambah mahasiswa
void tambahMahasiswa(Mhs **head) {
    Mhs *baru = (Mhs *)malloc(sizeof(Mhs));

    getchar();

    printf("Nama            : ");
    fgets(baru->nama, sizeof(baru->nama), stdin);
    baru->nama[strcspn(baru->nama, "\n")] = 0;

    printf("NIM             : ");
    scanf("%s", baru->nim);

    printf("Nilai Tugas     : ");
    scanf("%f", &baru->tugas);

    printf("Nilai UTS       : ");
    scanf("%f", &baru->uts);

    printf("Nilai UAS       : ");
    scanf("%f", &baru->uas);

    baru->nilaiAkhir = hitungNilaiAkhir(
        baru->tugas,
        baru->uts,
        baru->uas
    );

    baru->mutu = hitungMutu(baru->nilaiAkhir);

    baru->next = NULL;

    if (*head == NULL) {
        *head = baru;
    } else {
        Mhs *temp = *head;

        while (temp->next != NULL) {
            temp = temp->next;
        }

        temp->next = baru;
    }

    printf("\nData berhasil ditambahkan!\n");
}

// Tampilkan data
void tampilkanMahasiswa(Mhs *head) {

    if (head == NULL) {
        printf("\nData kosong!\n");
        return;
    }

    printf("\n=====================================================================\n");
    printf("%-15s %-10s %-8s %-8s %-8s %-12s %-5s\n",
           "Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai", "Mutu");
    printf("=====================================================================\n");

    Mhs *temp = head;

    while (temp != NULL) {

        printf("%-15s %-10s %-8.1f %-8.1f %-8.1f %-12.1f %-5c\n",
               temp->nama,
               temp->nim,
               temp->tugas,
               temp->uts,
               temp->uas,
               temp->nilaiAkhir,
               temp->mutu);

        temp = temp->next;
    }

    printf("=====================================================================\n");
}

// Cari mahasiswa
void cariMahasiswa(Mhs *head) {

    char cariNim[20];
    int ditemukan = 0;

    printf("Masukkan NIM yang dicari : ");
    scanf("%s", cariNim);

    Mhs *temp = head;

    while (temp != NULL) {

        if (strcmp(temp->nim, cariNim) == 0) {

            printf("\nData ditemukan\n");
            printf("Nama         : %s\n", temp->nama);
            printf("NIM          : %s\n", temp->nim);
            printf("Nilai Akhir  : %.1f\n", temp->nilaiAkhir);
            printf("Mutu         : %c\n", temp->mutu);

            ditemukan = 1;
            break;
        }

        temp = temp->next;
    }

    if (!ditemukan) {
        printf("\nData tidak ditemukan!\n");
    }
}

// Hapus mahasiswa
void hapusMahasiswa(Mhs **head) {

    char hapusNim[20];

    printf("Masukkan NIM yang dihapus : ");
    scanf("%s", hapusNim);

    Mhs *temp = *head;
    Mhs *prev = NULL;

    // Jika node pertama dihapus
    if (temp != NULL && strcmp(temp->nim, hapusNim) == 0) {
        *head = temp->next;
        free(temp);

        printf("Data berhasil dihapus!\n");
        return;
    }

    while (temp != NULL && strcmp(temp->nim, hapusNim) != 0) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Data tidak ditemukan!\n");
        return;
    }

    prev->next = temp->next;
    free(temp);

    printf("Data berhasil dihapus!\n");
}

// Simpan CSV
void simpanCSV(Mhs *head) {

    FILE *fp = fopen("data_mahasiswa.csv", "w");

    if (fp == NULL) {
        printf("File gagal dibuat!\n");
        return;
    }

    fprintf(fp, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    Mhs *temp = head;

    while (temp != NULL) {

        fprintf(fp,
                "%s,%s,%.1f,%.1f,%.1f,%.1f,%c\n",
                temp->nama,
                temp->nim,
                temp->tugas,
                temp->uts,
                temp->uas,
                temp->nilaiAkhir,
                temp->mutu);

        temp = temp->next;
    }

    fclose(fp);

    printf("Data berhasil disimpan ke data_mahasiswa.csv\n");
}

// Free memory
void freeMemory(Mhs *head) {

    Mhs *temp;

    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}