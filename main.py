def process_case(x, nums, acc=0):
    if x == 0 or not nums:
        return acc
    head, *tail = nums
    return process_case(x - 1, tail, acc + (head ** 4 if head <= 0 else 0))

def process_all_cases(n, lines, acc=[], idx=0):
    if n == 0:
        return acc
    x = int(lines[idx])
    nums = list(map(int, lines[idx + 1].split()))
    if len(nums) != x:
        result = -1
    else:
        result = process_case(x, nums)
    return process_all_cases(n - 1, lines, acc + [str(result)], idx + 2)

def main():
    import sys
    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    results = process_all_cases(n, lines[1:])
    print("\n".join(results))

if __name__ == "__main__":
    main()
