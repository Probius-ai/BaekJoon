import sys

N = int(sys.stdin.readline())

N_list = [int(sys.stdin.readline()) for _ in range(N)]

for i in sorted(N_list):
    sys.stdout.write(str(i) + '\n')