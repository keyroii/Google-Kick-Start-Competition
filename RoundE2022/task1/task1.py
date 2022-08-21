for testCase in range(int(input())):
    numberOfCells = int(input())

    if numberOfCells <= 0:
        botScore = 0
    elif numberOfCells <= 5:
        botScore = 1
    elif numberOfCells > 5:
        botScore = numberOfCells // 5
        remainder = numberOfCells % 5
        if remainder > 0:
            botScore += 1
    
    print(f"Case #{testCase+1}: {int(botScore)}")