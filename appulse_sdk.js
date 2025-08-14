const axios = require('axios');
const nodemailer = require('nodemailer');

class AppPulse {
    constructor(appName, version, statusUrl, alertEmail = null, errorThreshold = 5) {
        this.appName = appName;
        this.version = version;
        this.statusUrl = statusUrl;
        this.alertEmail = alertEmail;
        this.errorThreshold = errorThreshold; // percentuale errori oltre cui alert
        this.startTime = Date.now();
        this.requests = 0;
        this.errors = 0;

        // Configurazione default Nodemailer
        if (alertEmail) {
            this.transporter = nodemailer.createTransport({
                host: 'localhost', // sostituisci con il tuo SMTP
                port: 25,          // porta SMTP
                secure: false
            });
        }
    }

    recordRequest(success = true) {
        this.requests += 1;
        if (!success) this.errors += 1;
    }

    uptimePercentage() {
        if (this.requests === 0) return 100.0;
        return 100.0 * (this.requests - this.errors) / this.requests;
    }

    lastDeploy() {
        return new Date().toISOString();
    }

    status() {
        if (this.requests === 0) return "UP";
        const errorRate = (this.errors / this.requests) * 100;
        if (errorRate >= this.errorThreshold) return "WARNING";
        return "UP";
    }

    statusJson() {
        return {
            app_name: this.appName,
            version: this.version,
            status: this.status(),
            uptime_percentage: parseFloat(this.uptimePercentage().toFixed(2)),
            last_deploy: this.lastDeploy(),
            metrics: {
                requests: this.requests,
                errors: this.errors,
                avg_response_time_ms: 100 // logica reale opzionale
            },
            timestamp: new Date().toISOString()
        };
    }

    async sendStatus() {
        try {
            await axios.post(this.statusUrl, this.statusJson(), {
                headers: { 'Content-Type': 'application/json' }
            });
        } catch (err) {
            console.error('[AppPulse] Errore invio status:', err.message);
        }

        // Controllo alert email
        if (this.alertEmail && this.status() !== "UP") {
            this.sendEmailAlert();
        }
    }

    async sendEmailAlert() {
        try {
            const mailOptions = {
                from: '"AppPulse Alert" <alert@app-pulse.local>',
                to: this.alertEmail,
                subject: `[AppPulse ALERT] ${this.appName} status: ${this.status()}`,
                text: JSON.stringify(this.statusJson(), null, 2)
            };
            await this.transporter.sendMail(mailOptions);
            console.log(`[AppPulse] Alert inviato a ${this.alertEmail}`);
        } catch (err) {
            console.error('[AppPulse] Errore invio email:', err.message);
        }
    }
}

// ====== ESEMPIO DI USO ======
(async () => {
    const app = new AppPulse(
        "DemoApp",
        "v1.0.0",
        "http://localhost:5000/update_status",
        "tuo@email.com",
        5
    );

    app.recordRequest(true);
    app.recordRequest(false); // errore
    await app.sendStatus();
})();
