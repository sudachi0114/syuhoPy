import json
import smtplib
from email.mime.text import MIMEText

def readJson() -> dict:
    """ function read config.json file for get data to send Gmail
    Args:
        None
    Returns:
        data (dict): data of json
    """
    j = open("config.json", 'r')

    return json.load(j)


def main(data: dict) -> None:
    TO_ADDR = data['to_addr']
    FROM_ADDR = data['from_addr']

    print("SEND Gmail -----")
    print("  To  :",  TO_ADDR)
    print("  From:",FROM_ADDR)

    mail_id = FROM_ADDR
    mail_pass = input("confirm your passwd >>> ")

    # MAIL CONTENT -----
    MAIL_BODY = """This is Mail body \
    This mail send from python API \
    Daichi Suzuki."""

    SUBJECT = 'Hello from python'

    message = MIMEText(MAIL_BODY)  # 本文
    message['Subject'] = SUBJECT  # 件名
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
    data = readJson()
    main(data)
