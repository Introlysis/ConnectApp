import os

class Config:
    SECRET_KY = os.environ.get('SECRET_KEY') or 'Yeah, cool connect app bro'
