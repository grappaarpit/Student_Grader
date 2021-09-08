student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
#> Scores 91 - 100: Grade = "Outstanding"

#> Scores 81 - 90: Grade = "Exceeds Expectations"

#> Scores 71 - 80: Grade = "Acceptable"

#> Scores 70 or lower: Grade = "Fail"

student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇

for students in student_scores:
  if student_scores[students]>=91:
    student_grades[students] = "Outstanding"
  
  elif student_scores[students]>=81:
    student_grades[students] = "Exceeds Expectations"
  
  elif student_scores[students]>=71:
    student_grades[students] = "Acceptable"
  
  elif student_scores[students]<=70:
    student_grades[students] = "Fail"

  #student_grades[students] = 23
print(student_grades)
    

# 🚨 Don't change the code below 👇
#print(student_grades)





