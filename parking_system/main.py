import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import administrator, auth, customer, employee, role, vehicle

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(administrator.administrator_router)
app.include_router(auth.auth_router)
app.include_router(customer.customer_router)
app.include_router(employee.employee_router)
app.include_router(role.role_router)
app.include_router(vehicle.vehicle_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Parking System API."}


if __name__ == "__main__":
    port = os.getenv('PORT', default=8000)
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
