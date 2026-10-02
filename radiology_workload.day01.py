#Radiology Department Daily workload Tracker
# Day 01: Basics before conditional statements
department = input("enter department name:")
report_date = input("enter report date (YYYY-MM-DD:"))
xray_exams = int(input(enter xray examination:"))
ct_exams = int(input(enter ct examination:"))
mri_exams = int(input("enter MRI examination:"))
working_hours = float (input("enter working hours:"))
yesterday_total = int(input(enter yesterday's total examination:"))
daily_target = int(input(enter today 's workload target:"))
#Arithmetic calculation
total_exams = xray_exams + ct_exams + mri_exams
exams_per_hour = total_exams/working_hours
workload_change = total_exams - yesterday_total
#comparisons
target_reached = total_exams >= daily_target
busier_than_yesterday = total_exams > yesterday_total
#display the report
print("\nRadiology daily workload report")
print(f"department:{department}")
print(f"date:{report_date}")
print(f"X-ray examination:{xray_exams}") 
print(f"CT examination:{ct_exams}")
print(f"MRI examination:{mri_exams}")
print(f"total examination:{total_exam}")
print(f"average examination per hour :{exams_per_hour})
print(f"changed compared with yesterday:{workload_change}")
print(f"daily target reached:{target_reached}")
print(f"busier than yesterday:{busier_than_yesterday}")
