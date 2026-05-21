#include <stdio.h>
#include "linked_list.h"

int main() {

    Mhs *head = NULL;
    int pilihan;

    do {

        printf("\n===== SISTEM DATA MAHASISWA =====\n");
        printf("1. Tambah Mahasiswa\n");
        printf("2. Tampilkan Data\n");
        printf("3. Cari Mahasiswa\nll");
        printf("4. Hapus Mahasiswa\n");
        printf("5. Simpan ke CSV\n");
        printf("0. Keluar\n");

        printf("Pilih menu : ");
        scanf("%d", &pilihan);

        switch (pilihan) {

            case 1:
                tambahMahasiswa(&head);
                break;

            case 2:
                tampilkanMahasiswa(head);
                break;

            case 3:
                cariMahasiswa(head);
                break;

            case 4:
                hapusMahasiswa(&head);
                break;

            case 5:
                simpanCSV(head);
                break;

            case 0:
                freeMemory(head);
                printf("Program selesai.\n");
                break;

            default:
                printf("Pilihan tidak valid!\n");
        }

    } while (pilihan != 0);

    return 0;
}