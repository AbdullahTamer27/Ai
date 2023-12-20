def minimax(node, depth, maximizing_player):
  """
  Performs the minimax algorithm on a given game tree.

  Args:
    node: The current node in the game tree.
    depth: The current depth of the search.
    maximizing_player: Whether it is the maximizing player's turn.

  Returns:
    The minimax value of the node.
  """
  if depth == 0 or node.is_terminal():
    return node.value

  if maximizing_player:
    best_value = -float('inf')
    for child in node.children:
      best_value = max(best_value, minimax(child, depth - 1, False))
    return best_value
  else:
    best_value = float('inf')
    for child in node.children:
      best_value = min(best_value, minimax(child, depth - 1, True))
    return best_value

# Example usage
class Node:
  def __init__(self, value, children):
    self.value = value
    self.children = children

  def is_terminal(self):
    return len(self.children) == 0

# Create the game tree
root = Node(3, [
  Node(8, [
    Node(7, []),
    Node(1, []),
  ]),
  Node(2, [
    Node(3, []),
    Node(3, []),
  ]),
])

# Solve the game tree using minimax
best_value = minimax(root, 2, True)
print(f"The best value for the maximizing player is: {best_value}")