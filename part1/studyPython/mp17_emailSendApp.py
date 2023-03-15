import smtplib # send mail protocol
from email.mime.text import MIMEText

send_email = 'lty0880@naver.com'
send_pass = ''

recv_email = 'lty0880@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587

text = '''메일내용. 긴급.
조심. 빨리 연락.'''

msg = MIMEText(text)
msg['Subject'] = '메일 제목입니다'
msg['From'] = send_email # 보내는 메일
msg['To'] = recv_email # 받는 메일
print(msg.as_string())

mail = smtplib.SMTP(smtp_name, smtp_port) # CREATE SMTP OBJECT
mail.starttls() # 전송계층보안 시작 
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg=msg.as_string())
mail.quit()
print('전송완료')