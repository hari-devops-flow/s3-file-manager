import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = 'ap-south-1'  # change to your region
S3_BUCKET_NAME = 'HarisBucket'  # replace with your actual bucket name
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')  # default to SQLite if not set
DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 'yes']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else ['*']
SECRET_KEY = 'SECRET_KEY_PLACEHOLDER'  # replace with your actual secret key
