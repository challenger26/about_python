#import random lib since randint will be used in the program.
import random

#Generate and store variables needed to determine whether the user has enough
#time to get A.
hours_can_study_per_day = random.randint(0,2)
hours_needed_total = random.randint(0,20)
days_until_final = random.randint(0,10)

#Get hours the user has studied and convert the input into interget type in
#python.
hours_already_studied = int(input(
    "Please input how many hours you have studied (from 0 to 10): "))

#Print variables'values and descriptions, using concatenation.
print(hours_needed_total, "is the total number of hours you need to study.")
print(hours_can_study_per_day, "is the number of hours you can study per day.")
print(days_until_final, "is the days until final.")
print(hours_already_studied, "is total number of hours you have studied.")

#Define function can_study. The main functionality is to check whether the
#user have enough time to study to get A on the final.
def can_study(hours_can_study_per_day, hours_needed_total,
              hours_already_studied, days_until_final):
  #Calculate hours the user can study until final.
  hours_can_study_until_final = hours_can_study_per_day * days_until_final
  #Calculate hours the user's total study hours(including already studied).
  study_hours_total = hours_can_study_until_final + hours_already_studied
  
  #Checking whether the user's total study hours >= hours needed to get A. And
  #return it as the function's return value.
  return study_hours_total >= hours_needed_total

#Define function answer_question. The main functionality is to check whether the
#user have enough time to study to get A in the exam(by calling function
#can_study) and output the final result.
def answer_question(hours_can_study_per_day, hours_needed_total,
                    hours_already_studied, days_until_final):
  #Call function can_study to check whether the user can get A.
  can_get_A = can_study(hours_can_study_per_day, hours_needed_total,
                        hours_already_studied, days_until_final)
  
  #Print answer and return a boolean value indicating whether the user can get A.
  if (can_get_A):
    print("You can get an A on the final.")
    return True
  else:
    print("You cannot get an A on the final.")
    return False

# Call function answer_question to check whether the user can get A.
answer_question(hours_can_study_per_day, hours_needed_total, 
                hours_already_studied, days_until_final)

