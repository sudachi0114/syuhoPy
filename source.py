import smtplib
from email.mime.text import MIMEText

def main():
    TO_ADDR = 'to@gmail.com'
    FROM_ADDR = 'from@gmail.com'
    mail_id = FROM_ADDR
    mail_pass = input()

    message = MIMEText('Hello')  # 本文
    message['Subject'] = 'Hello from python'  # 件名
    message['From'] = FROM_ADDR  # 宛先
    message['To'] = TO_ADDR  # 送り主

    print("送信中.....")
    sender = smtplib.SMTP_SSL('smtp.gmail.com')
    sender.login(mail_id, mail_pass)
    sender.sendmail(FROM_ADDR, TO_ADDR, message.as_string())
    sender.quit()
    print("送信しました。")

if __name__ == '__main__':
    print("[Main]")
    main()
