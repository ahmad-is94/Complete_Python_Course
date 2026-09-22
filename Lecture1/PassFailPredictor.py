study_hours = float(input("Study hours: "))
attendance = float(input("Attendance %: "))
test_score = float(input("Previous test score: "))

if study_hours >= 2 and attendance >= 75 and test_score >= 50:
    result = "Pass"
else:
    result = "Fail"

print("Prediction:", result)
