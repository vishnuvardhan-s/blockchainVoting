# Access to this file : Election Head and Zone Representative

# if the voter forgets his email-ID his uniqueID can be used to retrive his emailID

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAG;'
                      'Database=VotingSystem;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
while (1):
    print('1.Find Unique ID\n2.Exit')
    i = int(input())
    if (i == 1):
        print('Enter the AADHAR number to find the unique ID')
        aadhar = input()
        cursor.execute(
            'select uniqueid,voterAadhar from RAG.VotingSystem.dbo.voters')
        flag = 0
        for row in cursor:
            s = ' '.join(str(x) for x in row)
            list = s.split()
            if (list[1] == aadhar):
                print('The Unique ID is ' + list[0])
                flag = 1
                break
        if (flag == 0):
            print('AADHAR Id not found')
    else:
        break
