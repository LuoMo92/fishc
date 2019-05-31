import requests
import bs4
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email():
    sender = '810754420@qq.com'
    receivers = ['810754420@qq.com']  # 接收邮件
    
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('可以查成绩啦~~~~~~~', 'plain', 'utf-8')
    message['From'] = Header("Python", 'utf-8')   # 发送者
    message['To'] =  Header("落墨", 'utf-8')        # 接收者
    
    subject = '2019年4月自考成绩查询'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP('smtp.qq.com',25)
        smtpObj.login(sender,"jigtnzntkipmbfgd")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

def open_url(url):
    # 使用代理
    # proxies = {"http": "127.0.0.1:1080", "https": "127.0.0.1:1080"}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)

    return res

def query(size):

    while size == 7 :
        time.sleep(100)
        host = "http://www.shmeea.edu.cn/page/24300/"
        req = open_url(host)
        # 解决中文乱码
        if req.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
        #如果设置为replace，则会用?取代非法字符；
        encode_content = req.content.decode(encoding, 'replace')

        soup = bs4.BeautifulSoup(encode_content, 'html.parser')
        size = int(soup.find('ul', id='changePage').div.text[3])
        print(time.ctime()+" "+"记录数:"+str(size))

def main():
    # 查询
    query(7)
    # 发送邮件
    send_email()

if __name__ == "__main__":
    main()