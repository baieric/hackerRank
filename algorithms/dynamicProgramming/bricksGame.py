# Solution to https://www.hackerrank.com/challenges/play-game
t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    # bunch of filler values so I don't need to check out of bounds all the time
    arr.extend([0,0,0,0,0,0])
    # max score if you are making a move at the current brick (with filler values)
    maxScore = [0 for x in range(n+7)]
    # the first brick's optimal move is always to take it
    maxScore[n-1] = arr[n-1]
    # best move (1, 2, or 3) to take
    bestMove = [0 for x in range(n)]
    # the first brick has a best move of "take 1 brick"
    bestMove[n-1] = 1
    index = n - 2
    while index >= 0:
        bestScore = 0
        # loop through taking 1, 2, or 3 bricks
        for j in range(1, 4):
            nextIndex = index + j
            score = 0
            if nextIndex < n:
                # add the optimal score of the remaining bricks
                score = maxScore[nextIndex+bestMove[nextIndex]]
            # add the points from the bricks taken
            for k in range(j):
                score = score + arr[index+k]
            if(score > bestScore):
                bestScore = score
                bestMove[index] = j
        maxScore[index] = bestScore
        index = index - 1
    print(maxScore[0])
