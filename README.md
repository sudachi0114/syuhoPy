# 週報自動送信プログラム

## Usage;

* please replace Gmail address for your condition.

```python:source.py
import smtplib
from email.mime.text import MIMEText

def main():
	""" PLEASE CHANGE HERE """
    TO_ADDR = 'to@gmail.com'
    FROM_ADDR = 'from@gmail.com'
```
