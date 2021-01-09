import re
import os
import gspread

creds = gspread.service_account(filename="./creds.json")
client = creds.open_by_key('1IWjQHoVbPxbmuoXbcOukx7G0lQxrbHxTKQHO7tym27U')


def getSubject():

    subject=""

    for _, __, files in os.walk('./'):

        for file in files:
            if(file.split('.')[0] in {'CN','ME','ET','SE','AI','OOMD'}): 
                subject=file.split('.')[0]

    return subject




def getTodayAttendance( subject ):

    presentUSNs = set()
    usn_pattern = '1[Dd][Ss]1[1-9][a-zA-Z][a-zA-Z][0-9][0-9][0-9]'

    with open(f'{subject}.csv','r') as rf:
        for line in rf:
            usn = re.search(usn_pattern,line)
            if (usn): presentUSNs.add( str(usn.group(0).upper()) )

    return presentUSNs
            



def UpdateAttendanceSheet( subject, presentUSNs):

    subjectID={ 'CN' : 0,'ET' : 1, 'AI' : 2, 'SE' : 3, 'ME' : 4, 'OOMD' : 5 }
    index=subjectID[subject]


    sheet=client.get_worksheet(index)
    data=sheet.get_all_records()

    for row in range(len(data)):

        print(data[row])
        
        if(data[row]['USN'] in presentUSNs):
            sheet.update_cell(row+2,3, data[row]['Attendance']+1)

        




if __name__ == "__main__":
    
    subject = getSubject()

    todayAttendance = getTodayAttendance( subject  )

    UpdateAttendanceSheet( subject, todayAttendance )

        
        






