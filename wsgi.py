"""
WSGI entry point for production deployment.
Use with gunicorn: gunicorn wsgi:app
"""

import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app
from flasgger import Swagger

app = create_app(os.environ.get('FLASK_ENV', 'production'))

# Initialize Swagger for API documentation
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "PassForge AI API",
        "description": "Password Management & Analysis API",
        "version": "1.0.0"
    },
    "basePath": "/api"
})

if __name__ == '__main__':
    app.run()
