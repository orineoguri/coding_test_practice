def solution(N):
    if N == 1:
        return 4
    elif N == 2:
        return 6
    else:
        memory = [0]*N
        memory[0] = 4
        memory[1] = 6
        for i in range(2,N):
            memory[i] = memory[i-1] + memory[i-2]

        return memory[-1]