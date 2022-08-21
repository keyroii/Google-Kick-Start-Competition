from itertools import islice

def isPalindrom(str):
    return str == str[::-1]

for testCase in range(int(input())):
    strLength = int(input())
    palindrom = input()

    palindromList = [*palindrom]
    uniqueChars = len(set(palindromList))
    if uniqueChars == 1:
        print(f"Case #{testCase+1}: {palindromList[0]}")
        continue
    
    for i in range(uniqueChars, strLength+1):
        if isPalindrom(palindrom[:i]) and len(palindromList) % i == 0:
            break
    
    
    print(f"Case #{testCase+1}: {palindrom[:i]}")