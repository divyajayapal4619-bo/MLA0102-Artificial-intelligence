N = 12

board = [-1] * N

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True

def solve(row):
    if row == N:
        return True
    for col in range(N):
        if safe(row, col):
            board[row] = col
            if solve(row+1):
                return True
    return False

solve(0)

for i in range(N):
    print("." * board[i] + "Q" + "." * (N-board[i]-1))
