def solution(participant, completion):
    p_dict = dict.fromkeys(participant, 0)
    for p in participant:
        p_dict[p] += 1
    for c in completion:
        p_dict[c] -= 1
    for p in p_dict:
        if p_dict[p] > 0:
            return p