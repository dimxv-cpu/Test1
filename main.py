

from fastapi import FastAPI
from fastapi.responses import FileResponse
from datetime import datetime

app = FastAPI()

@app.get("/get-date")
def get_date():
    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a text file with the date inside
    file_name = "current_date.txt"
    with open(file_name, "w") as f:
        f.write(f"Current date and time: {current_date}\n")

    # Return the file as a downloadable response
    return FileResponse(path=file_name, filename=file_name, media_type="text/plain")

@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/")
def read_root():
    return {"message": "Hello, Render!"}



