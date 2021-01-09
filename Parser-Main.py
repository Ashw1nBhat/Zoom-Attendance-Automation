import csv
import re

usn_pattern = '1[Dd][Ss]1[1-9][a-zA-Z][a-zA-Z][0-9][0-9][0-9]'
raw = []
curr_attendance = []

with open('Raw Data.csv','r') as rf:
    for line in rf:
        usn = re.search(usn_pattern,line)
        if usn:
            raw.append(str(usn.group(0).upper()))
            
with open("Today's Attendance.csv",'r') as rf:
    attendance_reader = csv.DictReader(rf)
    

    for row in attendance_reader:
        for line in raw:
            if line == row['USN']:
                curr_attendance.append({'USN': row['USN'],'Attendance': str(int(row['Attendance'])+1)})
                break
        else:
            curr_attendance.append({'USN': row['USN'],'Attendance': row['Attendance']})
                

with open("Today's Attendance.csv",'w',newline='') as wf:
    fieldnames = ['USN','Attendance']
    attendance_writer = csv.DictWriter(wf,fieldnames=fieldnames)
    attendance_writer.writeheader()

    for usn in curr_attendance:
        attendance_writer.writerow(usn)

    
        
        






