"""Example entry point; replace board to try another position."""

from checkmate import checkmate


def main():
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)


if __name__ == "__main__":
    main()
