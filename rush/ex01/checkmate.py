def print_pretty_board(board_str):
    for r in board_str.strip().split('\n'):
        print(' '.join(list(r)))

def checkmate(board_str):
    print_pretty_board(board_str)
    
    rows = board_str.strip().split('\n')
    size = len(rows)
  
    if size == 0 or any(len(r) != size for r in rows):
        print("Error")
        return
    kings = [(r, c) for r in range(size) for c in range(size) if rows[r][c] == 'K']
    if len(kings) != 1:
        print("Error")
        return
        
    kr, kc = kings[0]

    def look(dr, dc):
        r, c = kr + dr, kc + dc
        steps = 1 
        while 0 <= r < size and 0 <= c < size:
            if rows[r][c] != '.':
                return rows[r][c], steps
            r += dr
            c += dc
            steps += 1
        return None, 0 

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        piece, steps = look(dr, dc)

        if piece in ['R', 'Q']:
            print("Success")
            return
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        piece, steps = look(dr, dc)
        if piece in ['B', 'Q']:
            print("Success")
            return

        if piece == 'P' and steps == 1:
            print("Success")
            return
    print("Fail")


def main():
    board = """\
......
...B..
..K...
...R..
.R....
......
"""
    checkmate(board)

if __name__ == "__main__":
    main()
