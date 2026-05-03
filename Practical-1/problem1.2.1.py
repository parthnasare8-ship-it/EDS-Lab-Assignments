n = int(input())
marks = list(map(int, input().split()))

if min(marks) < 40:
    print("Fail")
else:
    p = sum(marks) / n
    print(f"Aggregate Percentage: {p:.2f}")
    if p > 75:
        print("Grade: Distinction")
    elif p >= 60:
        print("Grade: First Division")
    elif p >= 50:
        print("Grade: Second Division")
    else:
        print("Grade: Third Division")
