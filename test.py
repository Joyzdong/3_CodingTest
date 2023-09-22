import collections
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return answer.popitem()[0]
    return list(answer)[0]

r = solution(participant, completion)
print(r)