def solution(n):
    
    memory = [1] * (n+1)
    
    for i in range(2, n+1):
            memory[i] = (memory[i-1] + memory[i-2]) % 1000000007
    
    return memory[n]