def jumpingOnClouds(c):
    minJumps = 0
    index = 0
    n = len(c)
    while index < n:
        try:
            if index == n - 1:
                return minJumps
            if index + 2 >= n:
                return minJumps + 1
            else:
                if c[index + 2] == 0:
                    index = index + 2
                else:
                    index = index + 1
                minJumps = minJumps + 1 
        except:
            return minJumps

#MAIN
# 0 0 0 1 0 0
# 0 0 1 0 0 1 0
c = list(map(int, input().rstrip().split()))

d = list(map(int, input().rstrip().split()))

print(jumpingOnClouds(c))
print(jumpingOnClouds(d))