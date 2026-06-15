"""PassForge AI - AI-Powered Password Strength & Breach Detector."""

import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app()

if __name__ == '__main__':
    print("\n🔐 PassForge AI Starting...\n✅ AI Model Ready\n🌐 http://127.0.0.1:5000\n")
    
    app.run(
        debug=os.environ.get('FLASK_ENV') == 'development',
        host='127.0.0.1',
        port=5000
    )
