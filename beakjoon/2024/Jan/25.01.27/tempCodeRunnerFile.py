    if DP[y][x] == DP[y-1][x] and y > 0:
      LCS(y - 1, x, result)

    elif DP[y][x] == DP[y][x-1] and x > 0:
      LCS(y, x - 1, result)