import random
from colorama import Fore

levels = {
    1: {"max": 10, "attempts": 3},
    2: {"max": 50, "attempts": 5},
    3: {"max": 100, "attempts": 7}
}

def play_game(level):
    max_number = levels[level]["max"]
    attempts = levels[level]["attempts"]

    secret_number = random.randint(1, max_number)

    print(Fore.CYAN + f"\n=== LEVEL {level} ===")
    print(f"Tebak angka 1 - {max_number}")
    print(f"Kesempatan: {attempts} kali")

    while attempts > 0:
        try:
            guess = int(input("Masukkan tebakan: "))

            if guess == secret_number:
                print(Fore.GREEN + "Benar! Kamu menang!")
                score = attempts * 10
                print(Fore.YELLOW + f"Skor level ini: {score}")
                return score

            elif guess < secret_number:
                print(Fore.MAGENTA + "Angka terlalu kecil!")

            else:
                print(Fore.RED + "Angka terlalu besar!")

            attempts -= 1
            print(Fore.YELLOW + f"Sisa percobaan: {attempts}")

        except ValueError:
            print(Fore.RED + "Input harus angka!")

    print(Fore.RED + f"Game Over! Angkanya adalah {secret_number}")
    return 0