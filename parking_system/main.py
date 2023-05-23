import os
from typing import Union
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import administrator, auth, customer, employee, reservations, role, vehicle, parking, pay
from api.dependencies import get_current_user
from data.models import Administrator, Customer, Employee
from schemas.administrator import Administrator as ASchema
from schemas.customer import Customer as CSchema
from schemas.employee import Employee as ESchema


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(administrator.administrator_router)
app.include_router(auth.auth_router)
app.include_router(customer.customer_router)
app.include_router(employee.employee_router)
app.include_router(reservations.reservation_router)
app.include_router(role.role_router)
app.include_router(vehicle.vehicle_router)
app.include_router(parking.parking_router)
app.include_router(pay.pay_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Parking System API."}


@app.get("/me", response_model=Union[ASchema, CSchema, ESchema], tags=["User"])
def get_me(user: Union[Administrator, Customer, Employee] = Depends(get_current_user)):
    return user


if __name__ == "__main__":
    port = os.getenv("PORT", default=8000)
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))
