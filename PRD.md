# PRD – AppPulse: Centralized App Monitoring Dashboard

## 1. Titolo
**AppPulse – Centralized App Monitoring Dashboard**

## 2. Obiettivo
Creare una piattaforma centrale per monitorare lo stato di tutte le app in sviluppo, ricevere alert automatici in caso di downtime e avere metriche sul ciclo di vita di ogni app.

## 3. Stakeholders
- **Product Owner**: tu
- **Dev Team**: sviluppatori delle singole app
- **IT / Operations**: per deploy e alerting
- **Dashboard Viewer**: chiunque voglia verificare lo stato delle app

## 4. Funzionalità principali

### 4.1 Monitoring in tempo reale
- Health check per ogni app tramite endpoint `/status`
- Visualizzazione uptime, versione, stato corrente
- Aggregazione dei dati in tempo reale

### 4.2 Alerting automatico
- Notifiche su downtime o errori critici
- Canali supportati: Email, Slack, Telegram, webhook
- Configurazione soglie di alert personalizzabile

### 4.3 Storico e metriche
- Cronologia uptime/down
- Timeline dei deploy per ogni app
- Errori e crash log storicizzati
- Metriche di sviluppo: feature completate, tempo medio tra fix

### 4.4 Fil rouge di sviluppo
- Template di progetto uniforme
- Logging standardizzato (JSON schema condiviso)
- Endpoint health check `/status` obbligatorio
- CI/CD pipeline unificata (GitHub Actions / Jenkins)

### 4.5 Frontend Dashboard
- Interfaccia grafica con:
  - Tabella stato app
  - Grafici uptime e trend deploy
  - Filtri per stato, versione, tipo di app
- Notifiche visive in caso di problemi

## 5. Requisiti tecnici

### 5.1 Backend
- Framework: FastAPI o Flask
- Database: PostgreSQL o SQLite
- API endpoints:
  - `GET /apps` – lista app con stato corrente
  - `POST /register` – registrazione nuova app
  - `GET /history/<app_id>` – storico uptime/errori
- Health check polling o webhook-based

### 5.2 Frontend
- Framework: React o Streamlit
- Visualizzazione:
  - Dashboard principale
  - Grafici uptime e deploy
  - Alert log

### 5.3 Alerting
- Configurabile per canale
- Soglie definibili per downtime o errori ripetuti

### 5.4 DevOps
- CI/CD unificata per tutte le app
- Template progetto condiviso
- Logging JSON standard

## 6. Fasi di implementazione
1. Definizione schema dati comune per tutte le app (`status.json`)
2. Setup database e backend
3. Prototipo frontend per una singola app
4. Implementazione health check e alerting
5. Estensione a tutte le app
6. Analisi metriche sviluppo e trend

## 7. KPI di successo
- 100% delle app registrate correttamente in dashboard
- Alert corretti al primo evento di downtime
- Visualizzazione uptime e storico deploy affidabile
- Uniformità dei log e health check tra tutte le app

## 8. Nome progetto
**AppPulse** – “tenere il polso” delle tue app in tempo reale.

## 9. Dashboard (Markdown Table)
| App Name | Status | Version | Uptime | Last Deploy | Alert |
|----------|--------|--------|--------|------------|-------|
| App1     | UP     | v1.2.0 | 99.9%  | 2025-08-14 | OFF   |
| App2     | DOWN   | v2.0.1 | 95.6%  | 2025-08-10 | ON    |

## 10. Flusso di alerting (codice)
```text
[App Status Endpoint] --> [Backend Polling / Webhook]
          |                            |
          v                            v
   Status OK / DOWN               Log & Store
          |                            |
          +------------> [Alert Manager] --+
                                         |
                                         v
                               [Email / Slack / Telegram]
```

## 11. Flusso CI/CD unificato (codice)
```text
[Developer Commit] --> [CI Pipeline: Build + Test]
          |                     |
          v                     v
    [Unit Tests]          [Integration Tests]
          |                     |
          +---------+-----------+
                    v
             [Deploy to AppPulse Monitoring]
```
### 12. Note

Tutte le app devono implementare endpoint /status standardizzato

Logging JSON uniforme per facilità aggregazione e metriche

Alerting configurabile per ogni app separatamente
