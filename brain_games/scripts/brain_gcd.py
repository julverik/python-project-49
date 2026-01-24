from brain_games.cli import welcome_user
from brain_games.game_engine import run_game
from brain_games.games.gcd import get_round_data


def main():
    welcome_user()
    run_game(get_round_data)


if __name__ == "__main__":
    main()