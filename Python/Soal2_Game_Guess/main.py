from colorama import init, Fore
from game import play_game
from scoreboard import save_score, show_top_scores

init(autoreset=True)

print(Fore.CYAN + "=== GUESS BATTLE GAME ===")

name = input("Masukkan nama pemain: ")

total_score = 0

for level in range(1, 4):
    score = play_game(level)
    total_score += score

print(Fore.YELLOW + f"\nTotal skor {name}: {total_score}")

save_score(name, total_score)

show_top_scores()