text = "((()))"
result = None

sum = 0
for l in text:
    if l == "(":
        sum += 1
    elif l == ")":
        sum -= 1

if sum == 0:
    result = "OK"
else:
    result = "FAIL"

print(result)
