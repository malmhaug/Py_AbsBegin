WAYS_TO_WIN = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8],
               [0, 3, 6],
               [1, 4, 7],
               [2, 5, 8],
               [0, 4, 8],
               [2, 4, 6]]

MOVE_ORDER = (4, 0, 2, 6, 8, 1, 3, 5, 7)

def analyze_moves(board, computer_sign):
    field_points = []
    lost_fields = []
    win_array = []
    best_moves = []
    field_count = 0
    optimal_moves = []

    # Put 10 points in the field which is owned by the computer or none
    for board_field in board:
        if board_field is ' ' or board_field is computer_sign:
            field_points.append(10)
        else:
            lost_fields.append(field_count)
            field_points.append(None)
        field_count += 1

    # Find the best moves based on the WAYS_TO_WIN
    for arrays in WAYS_TO_WIN:
        if field_points[arrays[0]] == 10 and field_points[arrays[1]] == 10 and field_points[arrays[2]] == 10:
            win_array.append(arrays)

    # Pick out the best moves
    for field in win_array:
        for number in field:
            if number not in best_moves:
                best_moves.append(int(number))

    # Put the best moves in order
    for order_number in MOVE_ORDER:
        if order_number in best_moves:
            optimal_moves.append(order_number)
    return optimal_moves

if __name__ == '__main__':
    print("Test: ")
    board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
    print(analyze_moves(board, 'O'))
