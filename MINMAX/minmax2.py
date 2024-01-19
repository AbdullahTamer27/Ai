def minimax(state, depth, player): #State = Currentstate // depth = Searchtree depth // Player to show if it is maximizing player or minimizing
    best = []

    if player == true: #if the player is a maximizing player then value from none to -infinity if minimizing then from none to infinity // bd2 mn none fel etnen 3shan deh el intial state
        best = [None, float('-inf')]
    else:
        best = [None, float('+inf')]

    if depth == 0 or game_over(state): #deh el base case hyrg3 el evaluation score bta3 el current state
        score = evaluate_state(state, player)
        undo_move(state, move, player)
        return [None, score]


def game_over(state):
    # Implement your game over logic here
    pass

def evaluate_state(state, player):
    # Implement your state evaluation logic here
    pass

def valid_moves(state, player):
    # Implement your logic to get valid moves for the player in the given state
    pass

def execute_move(state, move, player):
    # Implement logic to apply the move to the state
    pass

def undo_move(state, move, player):
    # Implement logic to undo the move in the state
    pass