values = tuple(map(int, input().split()))
def mean(values):
    sun = 0
    for i in (values):
        sun += i
    return sun
result = mean(values)
print(* values, result / len(values))