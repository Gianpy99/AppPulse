import time
import json
import smtplib
from datetime import datetime
from email.message import EmailMessage
import requests

class AppPulse:
    def __init__(self, app_name, version, status_url, alert_email=None, error_threshold=5):
        """
        app_name: nome dell'app
        version: versione corrente
        status_url: endpoint della dashboard
        alert_email: email per notifiche
        error_threshold: soglia errori % oltre cui inviare alert
        """
        self.app_name = app_name
        self.version = version
        self.status_url = status_url
        self.alert_email = alert_email
        self.error_threshold = error_threshold
        self.start_time = time.time()
        self.errors = 0
        self.requests = 0

    def record_request(self, success=True):
        self.requests += 1
        if not success:
            self.errors += 1

    def uptime_percentage(self):
        if self.requests == 0:
            return 100.0
        return 100.0 * (self.requests - self.errors) / self.requests

    def last_deploy(self):
        return datetime.utcnow().isoformat() + "Z"

    def status(self):
        if self.requests == 0:
            return "UP"
        error_rate = (self.errors / self.requests) * 100
        if error_rate >= self.error_threshold:
            return "WARNING"
        return "UP"

    def status_json(self):
        return {
            "app_name": self.app_name,
            "version": self.version,
            "status": self.status(),
            "uptime_percentage": round(self.uptime_percentage(), 2),
            "last_deploy": self.last_deploy(),
            "metrics": {
                "requests": self.requests,
                "errors": self.errors,
                "avg_response_time_ms": 100
            },
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

    def send_status(self):
        try:
            headers = {'Content-Type': 'application/json'}
            requests.post(self.status_url, data=json.dumps(self.status_json()), headers=headers)
        except Exception as e:
            print(f"[AppPulse] Errore invio status: {e}")

        # Controllo alert
        if self.alert_email and self.status() != "UP":
            self.send_email_alert()

    def send_email_alert(self):
        try:
            msg = EmailMessage()
            msg['Subject'] = f"[AppPulse ALERT] {self.app_name} status: {self.status()}"
            msg['From'] = "alert@app-pulse.local"
            msg['To'] = self.alert_email
            msg.set_content(json.dumps(self.status_json(), indent=2))

            # Configurazione SMTP: sostituisci con il tuo server SMTP
            with smtplib.SMTP('localhost') as smtp:
                smtp.send_message(msg)
            print(f"[AppPulse] Alert inviato a {self.alert_email}")
        except Exception as e:
            print(f"[AppPulse] Errore invio email: {e}")


# ====== ESEMPIO DI USO ======
if __name__ == "__main__":
    app = AppPulse(
        app_name="DemoApp",
        version="v1.0.0",
        status_url="http://localhost:5000/update_status",
        alert_email="tuo@email.com",
        error_threshold=5
    )

    # Simulazione di richieste
    app.record_request(success=True)
    app.record_request(success=False)  # errore
    app.send_status()
