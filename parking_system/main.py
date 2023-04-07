import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return { "message": "Welcome to Parking System API." }


if __name__ == "__main__":
    port = os.getenv('PORT', default=8000)
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
