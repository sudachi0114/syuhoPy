import json
import smtplib
from email.mime.text import MIMEText

def readJson(file_name: str="config.json") -> dict:
    """ function read config.json file for get data to send Gmail
    Args:
        file_name (str): JSON file name to read
    Returns:
        data (dict): data of json
    """
    f = open(file_name, 'r')

    return json.load(f)


def generate_message(data: dict) -> MIMEText:

    # MAIL CONTENT -----
    MAIL_BODY = data['mail_body']

    SUBJECT = data['mail_subject']

    message = MIMEText(MAIL_BODY)  # 本文
    message['Subject'] = SUBJECT  # 件名
    message['From'] = data['from_addr']  # 宛先
    message['To'] = data['to_addr']  # 送り主

    print("SEND Gmail ===============")
    print("  To  :",  message['To'])
    print("  From:", message['From'])
    print("----------")
    print("subject:", SUBJECT)
    print("body:")
    print(MAIL_BODY)
    print("----------")

    return message


def send(message: MIMEText) -> None:

    confirm = input("  送信して良いですか? [y/n] >>> ")
    if confirm == 'y':
        print("送信準備中.....")
        mail_pass = input("confirm your passwd >>> ")

        sender = smtplib.SMTP_SSL('smtp.gmail.com')
        sender.login(message['From'], mail_pass)

        sender.sendmail(message['From'], message['To'], message.as_string())
        print("送信しました。")
        sender.quit()
    else:
        print("aborted.")


def main():
    print("[Main]")
    data = readJson()
    message = generate_message(data)
    send(message)

if __name__ == '__main__':
    main()

