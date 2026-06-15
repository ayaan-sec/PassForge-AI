# 🔐 PassForge AI - Offline Password Management Platform

**100% Offline | AES-128 Encryption | No External APIs | Production Ready**

A complete password management system with hybrid strength analysis, secure vault, and REST API.

## ⚡ Quick Start

```bash
pip install -r requirements.txt
python run.py
```

**Access:** http://127.0.0.1:5000

## ✨ Features

✅ Encrypted vault (AES-128 Fernet)  
✅ Password analysis (zxcvbn + ML + local common passwords)  
✅ Secure generation (cryptographic randomness)  
✅ Bulk analysis (CSV/JSON files)  
✅ User authentication (Flask-Login)  
✅ Dashboard analytics with charts  
✅ REST API with Swagger docs  
✅ Custom password policies  
✅ 100% offline operation  

## 📦 Configuration

Create `.env`:
```env
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
SQLALCHEMY_DATABASE_URI=sqlite:///passforge.db
```

Generate SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## 🚀 Deployment

**Development:**
```bash
python run.py
```

**Production (Gunicorn):**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

**Docker:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:app"]
```

## 📚 API Endpoints

```
POST   /api/check              - Analyze password
POST   /api/generate           - Generate password
GET    /api/vault              - List entries
POST   /api/vault              - Add entry
GET    /api/vault/<id>         - Get entry
DELETE /api/vault/<id>         - Delete entry
GET    /api/dashboard/stats    - Get statistics
```

**Swagger UI:** http://127.0.0.1:5000/api/docs

## 📁 Structure

```
├── app/              # Flask application (routes, blueprints)
├── models/           # Database models (SQLAlchemy)
├── utils/            # Core logic (analysis, encryption, generation)
├── templates/        # HTML pages (14 files)
├── static/           # CSS & JavaScript
├── config/           # Configuration
├── run.py            # Development server
├── wsgi.py           # Production WSGI
└── requirements.txt  # Dependencies
```

## 🔐 Security

- **Encryption:** Fernet AES-128 for vault storage
- **Key Derivation:** PBKDF2 SHA256 (100k iterations)
- **Hashing:** Bcrypt for passwords
- **ORM:** SQLAlchemy (prevents SQL injection)
- **Protection:** CSRF, XSS prevention
- **Privacy:** 100% local, zero external calls

## 🎯 Usage

1. **Register** - Create account at http://127.0.0.1:5000
2. **Add Password** - Store in encrypted vault
3. **Check Password** - Real-time strength analysis
4. **Generate** - Create secure passwords
5. **Bulk Upload** - Analyze CSV/JSON files
6. **Dashboard** - View statistics and alerts

## ⚙️ Tech Stack

- Flask 3.0.0 (Web framework)
- SQLAlchemy 2.0.23 (ORM)
- zxcvbn 4.4.28 (Analysis)
- cryptography 41.0.7 (Encryption)
- pandas 2.1.3 (Data processing)
- flasgger 0.9.7.1 (Swagger/API docs)
- SQLite (Database)

## 🧪 Features Reference

| Feature | Endpoint | Details |
|---------|----------|---------|
| Login/Register | /auth | User authentication |
| Vault | /vault | Add/edit/delete/view passwords |
| Check | /dashboard/check-password | Analyze strength in real-time |
| Generate | /dashboard/generate-password | Create secure passwords |
| Bulk | /dashboard/bulk-analyze | Process CSV/JSON files |
| Policies | /dashboard/policies | Custom password rules |
| Stats | /dashboard | Dashboard & charts |
| API | /api/* | REST endpoints |

## 📊 Performance

- Password analysis: <100ms
- Bulk (1000 passwords): ~1 second  
- Lookup: O(1) in-memory
- Memory: <100MB idle

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Run: `pip install -r requirements.txt` |
| Database errors | Delete `passforge.db` and restart |
| Port 5000 in use | Change port in `run.py` line 31 |
| Templates not found | Verify `templates/` directory exists |
| CSS/JS not loading | Clear browser cache (Ctrl+Shift+Delete) |

## 📋 Requirements

- Python 3.9+
- pip
- ~50MB disk space
- No internet required

## 🎯 Status

✅ **Production Ready**  
✅ **All Features Complete**  
✅ **100% Offline**  
✅ **Enterprise Security**  

---

**Ready to secure your passwords?**

```bash
python run.py
```

For more details, see the source code comments and inline documentation.