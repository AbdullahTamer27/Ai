def minimax(state, depth, player): 
    best = []

    if player == true: 
    else:
        best = [None, float('+inf')]

    if depth == 0 or game_over(state): #
        score = evaluate_state(state, player)
        undo_move(state, move, player)
        return [None, score]


     for move in valid_moves(state, player):
        execute_move(state, move, player)
        _, score = minimax(state, depth - 1, -player)
        undo_move(state, move, player)
        #updating the best move based wether it is maximizing or minizing
        if player == 'max':  
            if score > best[1]:
                best = [move, score]
        else:
            if score < best[1]:
                best = [move, score]

    return best
