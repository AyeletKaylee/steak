from typing import List, Any


def merge_sort(seq: List[Any]):
    if len(seq) <= 1:
        return seq[:]

    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])

    return merge(left, right)


def merge(seq1, seq2):
    result = []
    ind1, ind2 = 0, 0
    while ind1 < len(seq1) and ind2 < len(seq2):
        if seq1[ind1] < seq2[ind2]:
            result.append(seq1[ind1])
            ind1 += 1
        else:
            result.append(seq2[ind2])
            ind2 += 1
            
    result.extend(seq1[ind1:] + seq2[ind2:])
    return result

print(merge_sort([8, 32, 92, 1, 3, 8, 9, 1]))
