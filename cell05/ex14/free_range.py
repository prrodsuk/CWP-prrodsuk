import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    step = 1 if start <= end else -1
    print(list(range(start, end + step, step)))
