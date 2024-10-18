#ระดับของคะแนนและเกรด
score = int(input("Enter score: "))
grade = 0

if score >= 80:
 grade = 4.0
elif score >= 75 and score < 80:
 grade = 3.5
elif score >= 70 and score < 75:
 grade = 3.0
elif score >= 65 and score < 70:
 grade = 2.5
elif score >= 60 and score < 65:
 grade = 2.0
elif score >= 55 and score < 60:
 grade = 1.5
elif score >= 50 and score < 55:
 grade = 0.1
else: grade = 0

score1 = int(input("Enter score: "))
grade1 = 0

if score1 >= 80:
 grade1 = 4.0
elif score1 >= 75 and score1 < 80:
 grade1 = 3.5
elif score1 >= 70 and score1 < 75:
 grade1 = 3.0
elif score1 >= 65 and score1 < 70:
 grade1 = 2.5
elif score1 >= 60 and score1 < 65:
 grade1 = 2.0
elif score1 >= 55 and score1 < 60:
 grade1 = 1.5
elif score1 >= 50 and score1 < 55:
 grade1 = 0.1
else: grade1 = 0

score2 = int(input("Enter score: "))
grade2 = 0

if score2 >= 80:
 grade2 = 4.0
elif score2 >= 75 and score2 < 80:
 grade2 = 3.5
elif score2 >= 70 and score2 < 75:
 grade2 = 3.0
elif score2 >= 65 and score2 < 70:
 grade2 = 2.5
elif score2 >= 60 and score2 < 65:
 grade2 = 2.0
elif score2 >= 55 and score2 < 60:
 grade2 = 1.5
elif score2 >= 50 and score2 < 55:
 grade2 = 0.1
else: grade2 = 0

score3 = int(input("Enter score: "))
grade3 = 0

if score3 >= 80:
 grade3 = 4.0
elif score3 >= 75 and score3 < 80:
 grade3 = 3.5
elif score3 >= 70 and score3 < 75:
 grade3 = 3.0
elif score3 >= 65 and score3 < 70:
 grade3 = 2.5
elif score3 >= 60 and score3 < 65:
 grade3 = 2.0
elif score3 >= 55 and score3 < 60:
 grade3 = 1.5
elif score3 >= 50 and score3 < 55:
 grade3 = 0.1
else: grade3 = 0
#ผลคะแนนของนาย Akwa Billy
print("Foundation English :" ,"score :",score,"=","grade :",grade )
print("General Business :" ,"score :",score1,"=","grade :",grade1 )
print("Introduction to Computer Systems :" ,"score :",score2,"=","grade :",grade2 )
print("Computer Programming :" ,"score :",score3,"=","grade :",grade3 )