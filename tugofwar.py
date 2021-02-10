"""
Created on 12/9/2020

@author: Albert
"""

def generate_lists(lst, pos, n, templst,d, used_idx):
    s = sum(lst)
    if pos < n:
        for i in range(len(lst)):
            if used_idx[i] == False:
                #print(lst)
                #print('old', used_idx)
                used_idx[i] = True
                #print('new', used_idx)
                for b in range(len(used_idx)):
                    if used_idx[b] == True and lst[b] == templst[pos]:
                        used_idx[b] = False
                #print('newnew', used_idx)
                templst[pos] = lst[i]
                #print(templst)
                b = templst[:]
                a = sum(b)
                if a not in d:
                   d[a] = []
                if b not in d[a]:
                    d[a].append(b)
                #print(d)
            generate_lists(lst, pos + 1, n, templst, d, used_idx)


def test(lst):
    n = len(lst) // 2
    templst = lst[:n]
    d = {}
    d[sum(templst)] = [templst[:]]
    used_idx = lst[:]
    for f in range(len(lst)):
        used_idx[f] = False
    for a in range(len(templst)):
        used_idx[a] = True
    #print(used_idx)
    generate_lists(lst, 0, n, templst, d,used_idx)
    s = sum(lst)

    least = sum(templst)
    # print(s, least)
    for k,v in d.items():
        least_diff = abs((s-least) - least)
        test_diff = abs((s-k)-k)
        # print(least_diff, test_diff)
        if test_diff < least_diff:
            least = k
    lst1 = d[least][0]
    lst2 = []
    for num in lst:
        if num not in lst1:
            lst2.append(num)
    ret1 = str(lst1)
    ret2 = str(lst2)

    print("The first subset is: " + ret1, sum(lst1))
    print("The second subset is: " + ret2, sum(lst2))

if __name__ == '__main__':
    example = [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
    #want [4, 100, 1, 23, 20] sum 148
    example2 = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    # want [45, -34, 12, 98, -1] sum 120
    a = [1,2,3,4,3]
    test(example2)


