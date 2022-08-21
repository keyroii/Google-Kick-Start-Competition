import bisect

for testCase in range(int(input())):
    numberStudents = int(input())
    studentRatings = {}
    students = list(map(int, input().split(' ')))
    for student in students:
        if(int(student) in studentRatings.keys()):
            studentRatings[int(student)] += 1
        else:
            studentRatings[int(student)] = 1
    ratingsSorted = sorted(studentRatings.keys())
    resultList = []

    for student in students:
        maxRating = student * 2
        result = bisect.bisect(ratingsSorted, maxRating)
        if result == 0:
            resultList.append(-1)
        if ratingsSorted[result-1] == student and studentRatings[ratingsSorted[result-1]] == 1:
            if(ratingsSorted[result-2] > maxRating):
                resultList.append(-1)
            else:
                resultList.append(ratingsSorted[result-2])
        else:
            resultList.append(ratingsSorted[result-1])


    print(f"Case #{testCase+1}: {' '.join(map(str, resultList))}")
