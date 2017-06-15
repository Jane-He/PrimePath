import unittest,time,smtplib,os
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

# ================定义发送邮件================
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("何娟娟————自动化测试报告", 'utf-8')
    msg['From'] = "m18271671622@163.com"
    msg['to'] = "2243369153@qq.com"

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("m18271671622@163.com", "hlj19930314")
    smtp.sendmail("m18271671622@163.com", "2243369153@qq.com", msg.as_string())
    smtp.quit()
    print("email has send out!")

# ===============查找测试报告目录，找到最新生成的测试报告文件================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == "__main__":
    test_dir = "F:\\VSCode\\Microsoft VS Code\\Projects\\PrimePath"
    test_report = "F:\\VSCode\\Microsoft VS Code\\Projects\\PrimePath\\report"

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_*.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '\\' + now + ' result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='PrimePath测试报告', description='用例执行情况:')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

    

    
   