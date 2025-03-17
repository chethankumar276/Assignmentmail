import smtplib
import random

def read_data_send_mail():
    try:
        f=open("emails.txt","r")
        emails=f.read()
        print(emails)

        emails=emails.split(",")
        print(emails)

    except:
        print("file not available")
    
    sender_email="*******" 

    for i in emails:
        otp_number=random.randint(00000,99999)
        print(otp_number)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(sender_email,"******")
        message=f"your OTP is {otp_number}"

        try:
            s.sendmail(sender_email,i,message)
            print("mail sent successfully")
            s.quit()
        except:
            print("mail noit sent")
read_data_send_mail()