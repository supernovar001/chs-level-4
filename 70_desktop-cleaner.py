def solution(wallpaper):
    m = len(wallpaper)
    n = len(wallpaper[0])
    #list_mn = [[0]* n for _ in range(m)]
    #print(list_mn)
   
    min_row, max_row = 50,0  #
    min_col, max_col = 50,0  #
    # make m list to (mxn) list
    for i in range(m):
        for j in range(n):
            if wallpaper[i][j] == "#" : #(행,열)
                min_row = min(min_row, i)
                min_col = min(j, min_col)
                max_row = max(min_row, i)
                max_col = max(j, min_col)

    return [min_row, min_col, max_row+1, max_col+1]
print(solution([".#...", "..#..", "...#."]))     #[0, 1, 3, 4] 

# # 최소, 최대 행 업데이트

