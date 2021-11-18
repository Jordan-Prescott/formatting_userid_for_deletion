Desctiption:

Desctiption:

This code is to format users ready for upload to Magic and then permantaly deleted from the system. This has two ways
of formatting the user. Option one which takes the whole number in the userID and option 2 which only uses the last 4 digits 
of the number. The final output is Magic template to delete users with the task ID, userID, Service provider, Group ID and Index 
in each row.

Example Input:
Number
3216549870
2164219846
2216461321
6549812123
3214684651
2168463522
1651874985
9431321642
3123131642
1981132168

Exammple output:
task,userId,serviceProviderId,groupId,index

user.delete,3098@domain.ev.com,ServiceP,MARSHA,1
user.delete,3010@domain.ev.com,ServiceP,MARSHA,2
user.delete,2046@domain.ev.com,ServiceP,MARSHA,3
user.delete,2024@domain.ev.com,ServiceP,MARSHA,4
user.delete,3063@domain.ev.com,ServiceP,MARSHA,5
user.delete,3087@domain.ev.com,ServiceP,MARSHA,6
user.delete,3038@domain.ev.com,ServiceP,MARSHA,7
user.delete,2009@domain.ev.com,ServiceP,MARSHA,8
user.delete,2003@domain.ev.com,ServiceP,MARSHA,9
user.delete,2246@domain.ev.com,ServiceP,MARSHA,10

Instructions:

1. Copy the whole of colunm A from your sheet including the title 'Number'
2. Paste this into Files/data.csv
3. Run the script in your IDE (Make sure your terminal is in the folder)
4. Upload Files/data.csv to Magic for deletion

**Remember when you run the script next to remove the existing data like the example above and replace with 
  your new colunm A.
