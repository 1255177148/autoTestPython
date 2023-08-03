from Conf.config import email_config
from Conf.config import smtp_config
import smtplib
import os
import logging
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header

logger = logging.getLogger('main.email')

class Email:
    def __init__(self, subject, context=None, attachments=None) -> None:
        """初始化邮件内容

        Args:
            subject (_type_): _邮件标题_
            context (_type_, optional): _邮件正文_. Defaults to None.
            attachments: _邮件附件,key为附件名称,value为附件_
        """
        self.subject = subject
        self.context = context
        self.attachents = attachments
        self.message = MIMEMultipart()
        self.message_init()
    
    
    def message_init(self):
        """初始化邮件数据

        Raises:
            ValueError: _description_
        """
        if self.subject:
            self.message['Subject'] = Header(self.subject, 'utf-8') # 邮件标题
        else:
            logger.error("不合法的邮件标题")
            raise ValueError("不合法的邮件标题")
        self.message['From'] = Header(email_config['from'])
        self.message['To'] = Header(email_config['receivers'])
        
        # 下面设置邮件正文
        if self.context:
            self.message.attach(MIMEText(self.context, 'html', 'utf-8')) # 邮件正文,以html的文本形式发送,以字符串文本发送，类型为plain
        if self.attachents:
            if isinstance(self.attachents, str):
                self.attach(self.attachents)
            if isinstance(self.attachents, list):
                for each in self.attachents:
                    self.attach(self.attachents)
    
    def attach(self, file):
        """将附件加进去

        Args:
            file : _附件地址_
        """
        attach = MIMEApplication(open(file, 'rb').read())
        attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
        attach['Content-Type'] = 'application/octet-stream'
        self.message.attach(attach)
    
    
    def sendEmail(self):
        smtp = smtplib.SMTP_SSL(smtp_config['host'], int(smtp_config['port']))
        result = True
        try:
            smtp.login(smtp_config['user'], smtp_config['passward'])
            print(self.message['From'])
            smtp.sendmail(email_config['sender'], (str(email_config['receivers'])).split(","), self.message.as_string())
        except Exception as e:
            result = False
            logger.error("发送邮件失败------>", exc_info=e)
        finally:
            smtp.close()

if __name__ == '__main__':
    context = '<p>这是一个测试邮件</p>'
    file = 'D://test.txt'
    
    email = Email('测试邮件', context=context, attachments=file)
    email.sendEmail()