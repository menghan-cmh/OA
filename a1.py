def main(source, target):
    if source == target:
        return 1

    for char in target:
        if not char in source:
            return -1
        

    # dp = []
    # for i in range(len(source)+1):
    #     dp.append([float('inf')] * (len(target)+1))

    # for i in range(len(source)+1):
    #     dp[i][0] = 0
    # for i in range(len(target)+1):
    #     dp[0][i] = -1

    # for i in range(1, len(source)+1):
    #     for j in range(1, len(target)+1):
    #         if ():
    #             dp[][] = min()

    # if dp[-1][-1] != float('inf'):
    #     return dp[-1][-1]
    # else:
    #     return -1
    

if __name__ == "__main__":
    source = "abc"
    target = "abcbc"

    output = 2
    assert main(source, target) == output
