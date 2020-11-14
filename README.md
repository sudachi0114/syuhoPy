# 週報自動送信プログラム

## Usage;

* **Only first-time** 

```
cp config.sample.json config.json
```

* **To Change Email configuration** please replace Here ⬇️.

```json:config.json
{
	"to_addr": "to@gmail.com",
	"from_addr": "from@gmail.com",
	"mail_subject": "mail subject",
	"mail_body": "Please write your message here.\nYour name."
}

```

* Send Email

```
python source.py
```

Please confirm email content.
And if it were looks good, then please input your Google Account Application Password.
