from pydantic import BaseModel


class NotificationBase(BaseModel):
    notification_type: str

    class Config:
        orm_mode = True


class Role(NotificationBase):
    id_notification: str

    class Config:
        orm_mode = True
