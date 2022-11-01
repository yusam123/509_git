from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

hon_board = [
    "......................",
    "################......",
    "#..............#......",
    "#..............#......",
    "#..............#####..",
    "#######............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.

    if input_board[x][y] == "#":
        return input_board
    if input_board[x][y] == old:
        input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
    if input_board[x-1][y] == old:
        input_board = flood_fill(input_board, old, new, x-1, y)
    if input_board[x+1][y] == old:
        input_board = flood_fill(input_board, old, new, x+1, y)
    if input_board[x][y-1] == old:
        input_board = flood_fill(input_board, old, new, x, y-1)
    if input_board[x][y+1] == old:
        input_board = flood_fill(input_board, old, new, x, y+1)



  

 

    
    return input_board

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

hon_modified_board = flood_fill(input_board=hon_board, old=".", new="~", x=5, y=12)

for a in hon_modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

###great coding