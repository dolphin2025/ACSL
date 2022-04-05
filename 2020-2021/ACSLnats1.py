

def find_max_sum_of_subrect(values): return max([sum([values.split()[i*int(values.split()[1])+j+2] for i in range(r1, r2+1) for j in range(c1, c2+1)]) for c1 in range(int(values.split()[1])) for c2 in range(c1,int(values.split()[1])) for r1 in range(int(values.split()[0])) for r2 in range(r1,int(values.split()[0]))])
    # inp = [int(i) for i in values.split()]
    # r, c = inp[0], inp[1]
    # inp = inp[2:]
    # # print(inp)
    # # print(r,c)
    # ar = [inp[c*i:c*(i+1)] for i in range (r)]
    # # print(ar)
    # ans = -10000000000
    # for r1 in range(r):
    #     for r2 in range(r1,r):
    #         for c1 in range(c):
    #             for c2 in range(c1,c):
    #                 s = 0
    #                 for i in range(r1, r2+1):
    #                     for j in range(c1, c2+1):
    #                         s += ar[i][j]
    #                 ans = max(ans, s)
    # return ans

print(find_max_sum_of_subrect('5 3 0 -2 -7 9 2 -6 -4 1 -4 -1 8 0 -2 -4 -3'))