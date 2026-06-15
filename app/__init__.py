"""PassForge AI - Simplified Password Analysis App."""

from flask import Flask
from flask_cors import CORS


def create_app():
    """Create Flask application."""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    CORS(app)
    
    @app.route('/')
    def index():
        """Serve main page."""
        return app.send_static_file('index.html')
    
    @app.route('/api/analyze', methods=['POST'])
    def analyze_password():
        """Analyze password strength and breach count."""
        from flask import request, jsonify
        from ai_model.analyzer import PasswordAnalyzerAI
        
        data = request.get_json()
        password = data.get('password', '')
        
        if not password:
            return jsonify({'error': 'Password required'}), 400
        
        analyzer = PasswordAnalyzerAI()
        result = analyzer.analyze(password)
        return jsonify(result)
    
    return app
