# Access to this file : Election Head and Zone Representative

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAG;'
                      'Database=VotingSystem;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
while (1):
    print('1.Validate voters\n2.List voters\n3.Display Voter Details\n4.Exit')
    i = int(input())
    if(i == 1):
        print('Enter the unique id ')
        uniqueid = input()
        print('Enter AADHAR number ')
        aadhar = input()
        flag = 0
        cursor.execute(
            'select uniqueid,voterAadhar,isVoted from RAG.VotingSystem.dbo.voters')
        for row in cursor:
            s = ' '.join(str(x) for x in row)
            list = s.split()
            if(list[0] == uniqueid and list[1] == aadhar and list[2] == 'false'):
                print('\n\nValid Candidate\n')
                string = "update voters set isVoted='true' where uniqueid='" + \
                    list[0]+"'"
                cursor.execute(string)
                cursor.commit()
                flag = 1
                break
        if(flag == 0):
            print('\n\nInvalid Candidate\n')
    elif(i == 2):
        cursor.execute('select * from voters')
        for row in cursor:
            print(row)
    elif (i == 3):
        print('Enter the uniqueID')
        uniqueid = input()
        string = "select * from voters where uniqueid='" + uniqueid + "'"
        cursor.execute(string)
        for row in cursor:
            print(row)
    else:
        break
