# 用于发送邮件的模块
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from config.smtp import SMTP_SERVER,SMTP_PORT,SMTP_SENDER,SMTP_RECEIVER,SMTP_USER,SMTP_PASS

# # 邮件标题
mail_title = '主题：考呀呀自动化测试报告@'+time.strftime("%Y%m%d")
print(mail_title)

# # 创建邮件发送对象, 普通的邮件发送形式
# # 数据在传输过程中会被加密。
smtp_obj = smtplib.SMTP_SSL(host=SMTP_SERVER)
# # 需要进行发件人的认证，授权。
# # smtp_obj就是一个第三方客户端对象
smtp_obj.connect(host= SMTP_SERVER, port=SMTP_PORT)

# 读取html文件内容
con= open('../report/html/report_test.html', 'rb')
mail_body = con.read()
con.close()

# 邮件内容, 格式, 编码
message = MIMEText(mail_body, 'html', 'utf-8')
message['From'] = SMTP_SENDER
message['To'] = SMTP_RECEIVER
message['Subject'] = Header(mail_title, 'utf-8')

# # 发送邮件
try:
    # # 如果使用第三方客户端登录，要求使用授权码，不能使用真实密码，防止密码泄露。
    res = smtp_obj.login(user=SMTP_USER, password = SMTP_PASS)
    print('登录结果：', res)
    smtp_obj.sendmail(SMTP_SENDER, SMTP_RECEIVER, message.as_string())
    print("发送邮件成功！！！")
    smtp_obj.quit()
except smtplib.SMTPException:
    print("发送邮件失败！！！")

