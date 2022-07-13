print("Введите N, M, K, x, y")
N, M, K, x_1, y_1 = int(input()), int(input()), int(input()), int(input()), int(input())
x_1 -= 1
y_1 -= 1
def solution(N, M, K, x_1, y_1):
    x_step =[1, 2, 2, 1, -1, -2, -2, -1]
    y_step =[2, 1, -1, -2, -2, -1, 1, 2]

    chance = [ [[0 for _ in range(M)] for _ in range(N)] for _ in range(K+1)]
    for x in range(N):
        for y in range(M):
            chance[0][x][y] = 1

    for k in range(1, K+1):
        for x in range(N):
            for y in range(M):
                curr_chance = 0
                for i in range(8):
                    if(0 <= x + x_step[i] < N) and (0 <= y + y_step[i] < M):
                        curr_chance += chance[k-1][y + y_step[i]][x + x_step[i]] / 8
                chance[k][y][x] = curr_chance
    return chance[K][x_1][y_1]

print(solution(N, M, K, x_1, y_1))