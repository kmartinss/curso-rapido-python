def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def resultado_final(**kwargs):
    print(kwargs['nome'])
       