"""Check whether the only king is attacked under the Rush00 rules."""


PIECES = "KPBRQ"
DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)


def parse_board(board):
    """Return square rows and the king position, or raise ValueError."""
    if not isinstance(board, str):
        raise ValueError("The board must be a string.")

    # Accept LF/CRLF and one final newline, without stripping empty squares.
    rows = board.replace("\r\n", "\n").split("\n")
    if rows[-1] == "":
        rows.pop()
    size = len(rows)
    if size == 0 or any(len(row) != size for row in rows):
        raise ValueError("The board must be a non-empty square.")

    kings = [
        (row, column)
        for row in range(size)
        for column in range(size)
        if rows[row][column] == "K"
    ]
    if len(kings) != 1:
        raise ValueError("The board must contain exactly one K.")
    return rows, kings[0]


def find_attackers(rows, king):
    """Look from the king along eight rays; the first piece blocks each ray."""
    size = len(rows)
    king_row, king_column = king
    attackers = []

    for row_step, column_step in DIRECTIONS:
        row = king_row + row_step
        column = king_column + column_step
        distance = 1
        diagonal = row_step != 0 and column_step != 0

        while 0 <= row < size and 0 <= column < size:
            piece = rows[row][column]
            if piece in PIECES:
                if (
                    piece == "Q"
                    or (piece == "B" and diagonal)
                    or (piece == "R" and not diagonal)
                    # Pawns attack upward, so an attacking pawn is below K.
                    or (piece == "P" and row_step == 1
                        and diagonal and distance == 1)
                ):
                    attackers.append((piece, row, column))
                break
            row += row_step
            column += column_step
            distance += 1

    return attackers


def analyze_board(board):
    """Validate a board and return rows, king position and attacking pieces."""
    rows, king = parse_board(board)
    return rows, king, find_attackers(rows, king)


def checkmate(board):
    """Print Success, Fail or Error, always followed by a newline."""
    try:
        rows, king, attackers = analyze_board(board)
    except ValueError:
        print("Error")
        return
    print("Success" if attackers else "Fail")
