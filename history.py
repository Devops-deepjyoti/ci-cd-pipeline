from github import Github
from datetime import datetime, timedelta
import pytz
import os


g = Github("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")

repo = g.get_repo("AcharyaBhattS/Project1_HV")

branch = g.get_repo("AcharyaBhattS/Project1_HV").get_branch("main")
# print(branch.commit.sha)
ShaVal = branch.commit.sha

# Script to check for the commit history and their time
commits = repo.get_commit(sha=ShaVal)
# print("Author: ",commits.commit.author)
print("Date: ",commits.commit.author.date)
commitTime = commits.commit.author.date
print("Commit Time: ",commitTime)

'''
ts_Commit = commitTime.timestamp()
print("Commit Timestamp: ",ts_Commit,"\n")
'''

# currentTime = str(datetime.now())
gmtTime = datetime.now(pytz.timezone('GMT'))
# ts_Now = gmtTime.timestamp()
# print("Current Time: ", currentTime)

# commitTime_d = commitTime.split(' ')[0]
# commitTime_t = commitTime.split(' ')[1]
# commitTime_d1 = commitTime_d.split('-')
# commitTime_t1 = commitTime_t.split(':')
# # commitTime_d11 = commitTime_d1.split(',')
 
# commitTime_dt = (commitTime_d1)+(commitTime_t1)
# print(commitTime_dt)

# currentTime_d = currentTime.split(' ')[0]
# currentTime_t = currentTime.split(' ')[1]
# currentTime_d1 = currentTime_d.split('-')
# currentTime_t1 = currentTime_t.split(':')
# print(currentTime_t1)
# currentTime_dt = (currentTime_d1)+(currentTime_t1)
# print(currentTime_dt)

# # datetime(year, month, day, hour, minute, second)
# currentTime_dt1 = datetime.datetime(currentTime_dt)
# commitTime_dt1 = datetime.datetime(commitTime_dt)

# # returns a timedelta object
# difference_dt = currentTime_dt1-commitTime_dt1 
# print('Difference: ', difference_dt)
  
# minutes = c.total_seconds() / 60
# print('Total difference in minutes: ', minutes)
  
# # returns the difference of the time of the day
# minutes = c.seconds / 60
# print('Difference in minutes: ', minutes)

# list1 = [1, 2, 3]
# str1 = ''.join(str(e) for e in list1)


todays_date = gmtTime

todays_day = todays_date.day
# print('Day: ', todays_day)
todays_month = todays_date.month
# print('Month: ', todays_month)
todays_year = todays_date.year
# print('Year: ', todays_date.year)
# to get hour from datetime
todays_Hr = todays_date.hour
# print('Hour: ', todays_Hr)
# # to get minute from datetime
todays_Minute = todays_date.minute
# print('todays_Minute: ', todays_date.minute)
# # to get minute from datetimecls
todays_Second = todays_date.second
# print('todays_Minute: ', todays_Second)

Present_Date = [todays_day, todays_month, todays_year, todays_Hr, todays_Minute, todays_Second]
print("Present_Date: ", Present_Date)

Commit_Date = [commitTime.day, commitTime.month, commitTime.year, commitTime.hour, commitTime.minute, commitTime.second]
print("Commit_Date: ", Commit_Date)

a = datetime(todays_date.year, todays_date.month, todays_date.day, todays_Hr, todays_Minute, todays_Second)
print(a)
b = datetime(commitTime.year, commitTime.month, commitTime.day, commitTime.hour, commitTime.minute, commitTime.second)
print(b)
  
# returns a timedelta object
c = a-b 
print('Difference: ', c)

if c < timedelta(minutes=5):
    print("Commit time is < 5")
    os.system("bash myScript.sh")
else:
    print("Commit time is >= 5")


    

# minutes = c.total_seconds() / 60
# print('Total difference in minutes: ', minutes)
  
# # returns the difference of the time of the day
# minutes = c.seconds / 60
# print('Difference in minutes: ', minutes)
