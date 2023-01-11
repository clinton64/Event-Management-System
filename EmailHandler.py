import email
from typing import List

from fastapi import FastAPI
from fastapi_mail import ConnectionConfig, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv 
import os
load_dotenv()

class EmailSchema(BaseModel):
    email: List[EmailStr]


creddentials={}
creddentials['EMAIL']=os.getenv('EMAIL')
creddentials['PASS']=os.getenv('PASS')
conf = ConnectionConfig(
    
    MAIL_USERNAME =creddentials['EMAIL'],
    MAIL_PASSWORD = creddentials['PASS'],
    MAIL_FROM = creddentials['EMAIL'],
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

#app = FastAPI()
html = """
<p>Thanks for using Fastapi-mail</p> 
"""
 
