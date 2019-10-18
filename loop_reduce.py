# we can reduce any range loops into at most 2 loops by using the following methods

import functools
def cartesian_product(s_lst, e_lst):
    if len(s_lst) != len(e_lst):
        raise ValueError('Length doesn\'t match.')
    
    n_loops = len(s_lst)
    buff_lst = s_lst.copy()
    times = functools.reduce(lambda x, y : (x * y), [e - s for s, e in zip(s_lst, e_lst)]) - 1 #the times it should run
    
    for s, e in zip(s_lst, e_lst):  #if any ending index is equal to or smaller than the starting index, the loop doesn't run
        if s >= e:
            return
    
    yield buff_lst
    
    for _ in range(times):
        for l in reversed(range(n_loops)):
            if buff_lst[l] + 1 == e_lst[l]: 
                buff_lst[l] = s_lst[l]
            else:
                buff_lst[l] += 1
                break
        yield buff_lst

if __name__ == '__main__':
    # for i in range(5):
    #     for j in range(6):
    #         for k in range(3):
    #             for l in range(2):
    #                 print(i, j, k, l)
    # becomes:
    # for x in cartesian_product([0, 0, 0, 0], [5, 6, 3, 2]):
    #     print(*x)
    
    # Example. Solve the puzzle "ABCD - ABC = DCDC" where A, B, C, D are distinct integers from 0-9
    s_lst = [1, 0, 0, 1]         # the starting index of A, B, C, D, note that A and D can't be 0
    e_lst = [10, 10, 10, 10]     # the ending index of A, B, C, D (exclusive in the loop)
    for lst in cartesian_product(s_lst, e_lst):
        [A, B, C, D] = map(str, lst)
        if len(set(lst)) != len(lst):  # since A, B, C, D are distinct, it filters the lists with replicated elements 
            continue
        ABC = int(A + B + C)
        ABCD = int(A + B + C + D)
        DCDC = int(D + C + D + C)
        if ABCD - ABC == DCDC:
            print(lst) 
    