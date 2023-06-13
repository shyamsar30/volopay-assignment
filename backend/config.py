from backend.env import Environment

class Config:
    APP_NAME = "vOLOPAY_ASSIGNMENT"
    DB_URL = Environment.DB_URL
    SWAGGER_UI_URL = "/wherearemyapis"