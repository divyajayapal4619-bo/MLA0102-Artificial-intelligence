# Minimax with Alpha-Beta Pruning

def minimax(node, depth, maximizing_player,
            alpha, beta):

    # Leaf node
    if not isinstance(node, list):

        print("Evaluating:", node)

        return node

    if maximizing_player:

        best = float("-inf")

        for child in node:

            value = minimax(
                child,
                depth + 1,
                False,
                alpha,
                beta
            )

            best = max(best, value)

            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:

                print("Pruned remaining MAX nodes")

                break

        return best

    else:

        best = float("inf")

        for child in node:

            value = minimax(
                child,
                depth + 1,
                True,
                alpha,
                beta
            )

            best = min(best, value)

            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:

                print("Pruned remaining MIN nodes")

                break

        return best


# Game tree
game_tree = [
    [
        [3, 5],
        [2, 9]
    ],
    [
        [12, 5],
        [23, 7]
    ]
]

print("Starting Minimax with Alpha-Beta Pruning\n")

best_value = minimax(
    game_tree,
    0,
    True,
    float("-inf"),
    float("inf")
)

print("\nBest value for MAX:", best_value)
