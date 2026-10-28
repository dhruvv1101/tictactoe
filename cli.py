"""Play Tic-Tac-Toe against the unbeatable AI in your terminal:  python cli.py"""
import random
from tictactoe.engine import best_move, winner, is_full


def show(b):
    cells = [c if c != " " else str(i + 1) for i, c in enumerate(b)]
    print("\n " + " | ".join(cells[0:3]) + "\n---+---+---\n " + " | ".join(cells[3:6])
          + "\n---+---+---\n " + " | ".join(cells[6:9]) + "\n")


def main():
    choice = ""
    while choice not in ("x", "o", "r"):
        choice = input("Play as X, O or R(andom)? ").strip().lower()
    human = random.choice("XO") if choice == "r" else choice.upper()
    ai = "O" if human == "X" else "X"
    print(f"You are {human}. X moves first. Cells are numbered 1-9.")
    board, turn = [" "] * 9, "X"
    while True:
        show(board)
        if turn == human:
            try:
                m = int(input("Your move (1-9): ")) - 1
                assert 0 <= m < 9 and board[m] == " "
            except (ValueError, AssertionError):
                print("Invalid move."); continue
            board[m] = human
        else:
            board[best_move(board, ai)] = ai
        w, _ = winner(board)
        if w or is_full(board):
            show(board)
            print(f"{w} wins!" if w else "Draw!")
            return
        turn = "O" if turn == "X" else "X"


if __name__ == "__main__":
    main()
