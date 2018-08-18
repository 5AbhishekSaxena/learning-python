a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))

# Test case in text file in same folder name as "testcase_for_superset"
