def solution(budgets, M):
    if sum(budgets) <= M : return max(budgets)
    
    budgets.sort()
    total = len(budgets)
    top = total
    bottom = 0
    estimated_cutline = budgets[-1]
    
    while(True):
        pivot = (top + bottom) // 2
        estimated_cutline = (M - sum(budgets[:pivot])) // (total - pivot)
        
        if estimated_cutline < budgets[pivot - 1]:
            top = pivot - 1
        elif estimated_cutline > budgets[pivot]:
            bottom = pivot + 1
        else:
            return estimated_cutline
        
        if top < bottom : break
            
    return estimated_cutline
        