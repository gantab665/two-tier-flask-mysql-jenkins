# Two-Tier Web App (Flask + MySQL) with Docker + Jenkins CI/CD

## Architecture
- Flask app container (port 5000)
- MySQL container (port 3306)
- Jenkins on the same EC2 triggers build + deploy on every GitHub push

## Run locally (on EC2)
```bash
docker compose up -d --build
curl http://localhost:5000/health
curl http://localhost:5000/init-db
curl http://localhost:5000/messages
