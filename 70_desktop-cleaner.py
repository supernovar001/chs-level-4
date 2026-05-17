def solution(wallpaper):

    # Initialization for Compare
    min_row , min_col = 50 , 50
    max_row, max_col = 0 , 0

    # From 1D list To 2D Matrix
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):

            if wallpaper[i][j] == "#" :
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    
    return [min_row, min_col, max_row+1, max_col+1] # +1 이유 : 문제 조건

print(solution([".#...", "..#..", "...#."]))  # [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))  # [1, 3, 5, 8]
