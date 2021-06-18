from fastapi import FastAPI, Form, BackgroundTasks
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import EmailStr
from typing import List



conf = ConnectionConfig(
    MAIL_USERNAME = "claytemateam@gmail.com",
    MAIL_PASSWORD = "iidvygzhbnfgoiwy",
    MAIL_FROM = "claytemateam@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True
)

app = FastAPI()


@app.post("/file")
async def send_file(
    background_tasks: BackgroundTasks,
    email:EmailStr = Form(...)
    ) -> JSONResponse:

    message = MessageSchema(
            recipients=[email],
            attachments=['text.txt']
            )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message,message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})