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
    def __init__(self, subject, context=None, **attachments) -> None:
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
    
    
    def message_init(self):
        if self.subject:
            self.message['Subject'] = Header(self.subject, 'utf-8') # 邮件标题
        else:
            logger.error("不合法的邮件标题")
            raise ValueError("不合法的邮件标题")
        self.message['from'] = email_config['sender']
        self.message['to'] = email_config['receivers']
        
        # 下面设置邮件正文
        if self.context:
            self.message.attach(MIMEText(self.context, 'html', 'utf-8')) # 邮件正文，以html的文本形式发送
        
        