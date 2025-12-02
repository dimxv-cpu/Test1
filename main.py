

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from datetime import datetime

app = FastAPI()

app.get("/test-date")
def test_date(day: int = Query(..., ge=1, le=31),
              month: int = Query(..., ge=1, le=12),
              year: int = Query(..., ge=1)):
    try:
        custom_date = date(year, month, day)
    except ValueError:
        return {"error": "Invalid date provided."}

    file_name = "test_date.txt"
    with open(file_name, "w") as f:
        f.write(f"Provided date: {custom_date.strftime('%Y-%m-%d')}\n")

    return FileResponse(path=file_name, filename=file_name, media_type="text/plain")

# test with https://test1-b0f3.onrender.com/test-date?day=2&month=11&year=2025


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





