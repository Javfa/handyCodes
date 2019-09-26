solution = {}
@lru_cache(maxsize=2**10)
def edit_distance(str1, str2):
    if len(str1) == 0: return len(str2)
    if len(str2) == 0: return len(str1)
    
    tail_s1 = str1[-1]
    tail_s2 = str2[-1]
    
    candidates = [
        (edit_distance(str1[:-1], str2) + 1, 'DEL {} '.format(tail_s1)),
        (edit_distance(str1, str2[:-1]) + 1, 'ADD {} '.format(tail_s2)),
    ]
    if tail_s1 == tail_s2: 
        both_forward = (edit_distance(str1[:-1], str2[:-1]) + 0, ''.format(tail_s1))
    else:
        both_forward = (edit_distance(str1[:-1], str2[:-1]) + 1, 'SUB {} to {}'.format(tail_s1, tail_s2))   
    candidates.append(both_forward)
    
    min_distance, operation = min(candidates, key=lambda x: x[0])
    solution[(str1, str2)] = operation
    return min_distance
