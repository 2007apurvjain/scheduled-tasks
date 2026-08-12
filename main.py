import os
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

import datetime as dt
import pandas
import random
import smtplib
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
now = dt.datetime.now()
current_month=now.month
current_day = now.day

birthdays = pandas.read_csv("birthdays.csv")

for index,row in birthdays.iterrows():

    birth_month=(row["month"])
    birth_day=row["day"]
    name_of_person = row["name"]
    reciever_mail = row["email"]


    if birth_month==current_month and birth_day == current_day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            letter_lines = letter_file.read()

            letter_for_name = letter_lines.replace("[NAME]", name_of_person)
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(MY_EMAIL,reciever_mail,msg=f"Subject:Happy Birthday!!!!!\n\n{letter_for_name}")









# 4. Send the letter generated in step 3 to that person's email address.




