def solution(begin, target, words):
    if target not in words : return 0
    
    word_len = len(begin)
    compare_list = [begin]
    candidate_list = []
    compare_level = 1
    used = {}
    for word in words : used[word] = False
    
    while(True):
        for compareing_word in compare_list:
            for word in words:
                mismatch_cnt = 0
                for i in range(word_len):
                    if compareing_word[i] != word[i]:
                        mismatch_cnt += 1
                if (mismatch_cnt < 2) and not used[word]:
                    candidate_list.append(word)
                    used[word] = True
        if target in candidate_list:
            return compare_level
        elif len(candidate_list) == 0:
            return 0
        else:
            compare_list = candidate_list
            candidate_list = []
            compare_level += 1
        