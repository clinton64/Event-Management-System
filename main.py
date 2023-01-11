# email
from fastapi_mail import FastMail, MessageSchema, MessageType
from starlette.responses import JSONResponse
from EmailHandler import EmailSchema, html, conf

from some_models import Event
from pdfHandler import generatePDF
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import postgresqlDB

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



#db = MysqlDB("db_Config.json")
db = postgresqlDB("db_Config.json")

@app.get('/')
def hello_world():
  return {'message' : 'hello world'}

data = ""
@app.get("/events/")
async def get_events():
  data = db.select()
  generatePDF(data)
  return {"data" : data}

@app.post("/events/create/")
async def create_event(event: Event):
  return {"data" : db.insert(event)}

@app.delete("/events/delete/{id}/")
async def delete_event(id:int):
  return {'data' : db.delete(id)}

@app.post("/email")
async def simple_send(email: EmailSchema) -> JSONResponse:
    message = get_MESSAGE(email)
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


def get_MESSAGE(email):
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),
        body=html,
        subtype=MessageType.html)
    return message