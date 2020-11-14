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


def main(data: dict) -> None:

    # MAIL CONTENT -----
    MAIL_BODY = data['mail_body']
    """
    MAIL_BODY = (
        "This is Mail body\n"
        "This mail send from python API\n"
        "\n"
        "Daichi Suzuki."
    )
    """

    SUBJECT = 'Hello from python'

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


    
    confirm = input("  送信して良いですか? [y/n] >>> ")
    if confirm == 'y':
        print("送信準備中.....")
        mail_pass = input("confirm your passwd >>> ")

        sender = smtplib.SMTP_SSL('smtp.gmail.com')
        sender.login(message['To'], mail_pass)

        sender.sendmail(message['From'], message['To'], message.as_string())
        print("送信しました。")
        sender.quit()
    else:
        print("aborted.")


if __name__ == '__main__':
    print("[Main]")
    data = readJson()
    main(data)

