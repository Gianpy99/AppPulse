# AppPulse – Centralized App Monitoring Dashboard

## Overview
**AppPulse** centralizza il monitoraggio di tutte le tue app, con alert automatici, storico uptime, deploy tracking e dashboard interattiva. Standardizza sviluppo e CI/CD tra progetti.

## Funzionalità principali
- Monitoraggio in tempo reale di tutte le app
- Alert automatici su downtime o errori
- Storico uptime, errori e deploy
- Dashboard web con filtri e grafici
- Template JSON standard per status e alert

## Status JSON (template in-line)
```json
{
  "app_name": "App1",
  "version": "v1.0.0",
  "status": "UP",
  "uptime_percentage": 99.9,
  "last_deploy": "2025-08-14T12:00:00Z",
  "metrics": {
    "requests": 1024,
    "errors": 2,
    "avg_response_time_ms": 120
  },
  "timestamp": "2025-08-14T12:00:00Z"
}
```

## Alert JSON (template in-line)
```json
{
  "app_name": "App1",
  "alerts": [
    {
      "type": "downtime",
      "threshold_seconds": 60,
      "channels": ["email", "slack"]
    },
    {
      "type": "error_rate",
      "threshold_percentage": 5,
      "channels": ["telegram"]
    }
  ]
}
```

## Setup rapido

### Backend
```bash
git clone https://github.com/tuo-username/AppPulse.git
cd AppPulse/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd ../frontend
npm install
npm start
```

## Registrare una nuova app
```bash
POST /register
{
  "app_name": "NomeApp",
  "status_url": "https://app.example.com/status"
}
```

## Dashboard (tabella esempio)
| App Name | Status | Version | Uptime | Last Deploy | Alert |
|----------|--------|--------|--------|------------|-------|
| App1     | UP     | v1.2.0 | 99.9%  | 2025-08-14 | OFF   |
| App2     | DOWN   | v2.0.1 | 95.6%  | 2025-08-10 | ON    |

## Repository structure
```
AppPulse/
├── README.md
├── PRD.md
├── status_template.json
├── alert_config.json
├── backend/
│   └── ... FastAPI/Flask code ...
├── frontend/
│   └── ... React/Streamlit code ...
└── ci_cd/
    └── ... pipeline templates ...
```

## Contribuire
1. Forka il repo
2. Crea branch: `git checkout -b feature/my-feature`
3. Commit & push
4. Apri PR

## Licenza
MIT License

## PRD Sintetico
**Obiettivo:** centralizzare monitoraggio, alerting, deploy tracking e standardizzare metriche e CI/CD tra tutte le app.

**Requisiti funzionali:**
1. Registrazione e gestione app
2. Raccolta status JSON standard
3. Alert automatici su downtime o errori
4. Dashboard interattiva
5. Storico metriche e uptime
6. Fil-rouge tra tutte le app

**Requisiti non funzionali:**
- Scalabilità e resilienza
- Alert immediati
- Database persistente
- UI chiara e mobile-friendly
