# 🔍 Log Analyzer & Alert System

## 🇬🇧 English

🛡️ **Python mini-SIEM** that parses log files (`auth.log`), applies YAML-based detection rules, generates security alerts (e.g. SSH brute‑force), sends email notifications, indexes alerts in Elasticsearch and visualizes them in Grafana.

---

### 🎯 Project Purpose
- 💻 Practice hands-on skills as a **Cybersecurity Engineer**  
- 🛠️ Build a simple yet extensible detection engine  
- 🚀 Simulate a real-world automated security alert flow  

---

### 🗂 Project Structure

```
log-analyzer-alert-system/
│
├── src/
│   ├── analyze_logs.py
│   ├── generate_synthetic_alerts.py
│   ├── utils/
│   │   ├── alert.py
│   │   └── detect.py
│   └── tests/
│       └── test_email.py
│
├── config/
│   ├── config.yaml             # (excluded in .gitignore)
│   └── config.example.yaml     # Safe template version
│
├── rules/
│   └── detection_rules.yaml
│
├── logs/
│   └── auth.log
│
├── output/
│   └── alerts.json
│
├── dashboards/
│   └── log_alerts_dashboard.json
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

### ⚙️ Setup & Usage

1. **Clone** the repository:
   ```bash
   git clone https://github.com/your-username/log-analyzer-alert-system.git
   cd log-analyzer-alert-system
   ```
2. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure** your `config/config.yaml` from the example:
   ```yaml
   email:
     enabled: true
     smtp_server: "smtp.gmail.com"
     port: 465
     username: "you@example.com"
     password: "••••••••••••"
     from: "you@example.com"
     to: "alert@company.com"
   ```
4. **Run** log analysis and alert detection:
   ```bash
   python src/analyze_logs.py
   ```
5. **Import** the Grafana dashboard:
   ```bash
   docker-compose up -d
   ```
   - Open Grafana → **+ → Import**
   - Upload `dashboards/log_alerts_dashboard.json`
   - Select **Elasticsearch**
   - Use index pattern `log_analyzer_alerts*`, time field `ingest_timestamp`

---

### 📊 Grafana Dashboard

1. **Latest Alerts**  
2. **Top 10 Offenders**  
3. **Alert Count Over Time**

---

### 🔧 Technologies Used

- **Python 3** 🐍  
- **PyYAML**  
- **Regex**  
- **smtplib / EmailMessage**  
- **Elasticsearch** (Docker)  
- **Grafana** (Docker)  
- **JSON, YAML**

---

### 🔜 Possible Extensions

- nginx / fail2ban / Windows Event Log  
- SQLite or CSV export  
- Dockerized analyzer + CI/CD  
- Prometheus & Loki integration

---

## 🇮🇹 Italiano

🛡️ **Mini-SIEM in Python** che analizza file di log (`auth.log`), applica regole di detection definite in YAML, genera alert di sicurezza (es. brute‑force SSH), invia notifiche via email, indicizza gli alert in Elasticsearch e li visualizza in Grafana.

---

### 🎯 Scopo del progetto
- 💻 Allenare competenze pratiche da **Cybersecurity Engineer**  
- 🛠️ Costruire un motore di detection semplice ma estendibile  
- 🚀 Simulare un flusso reale di **alert** di sicurezza automatizzati  

---

### 🗂 Struttura del progetto

```
log-analyzer-alert-system/
│
├── src/
│   ├── analyze_logs.py
│   ├── generate_synthetic_alerts.py
│   ├── utils/
│   │   ├── alert.py
│   │   └── detect.py
│   └── tests/
│       └── test_email.py
│
├── config/
│   ├── config.yaml             # (escluso via .gitignore)
│   └── config.example.yaml     # Versione senza credenziali
│
├── rules/
│   └── detection_rules.yaml
│
├── logs/
│   └── auth.log
│
├── output/
│   └── alerts.json
│
├── dashboards/
│   └── log_alerts_dashboard.json
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

### ⚙️ Setup e utilizzo

1. **Clona** la repository:
   ```bash
   git clone https://github.com/tuo-username/log-analyzer-alert-system.git
   cd log-analyzer-alert-system
   ```
2. **Installa** le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
3. **Copia e configura** il file `config/config.yaml` da `config.example.yaml`:
   ```yaml
   email:
     enabled: true
     smtp_server: "smtp.gmail.com"
     port: 465
     username: "iltuoindirizzo@gmail.com"
     password: "••••••••••••"
     from: "iltuoindirizzo@gmail.com"
     to: "target@azienda.com"
   ```
4. **Esegui** l’analisi:
   ```bash
   python src/analyze_logs.py
   ```
5. **Importa** la dashboard in Grafana:
   ```bash
   docker-compose up -d
   ```
   - Grafana → **+ → Import**
   - Carica `dashboards/log_alerts_dashboard.json`
   - Seleziona data source **Elasticsearch**
   - Usa index pattern `log_analyzer_alerts*`, campo tempo `ingest_timestamp`

---

### 📊 Dashboard Grafana

1. **Latest Alerts**  
   - Tabella con gli ultimi alert  
2. **Top 10 Offenders**  
   - Grafico a barre degli IP più attivi  
3. **Alert Count Over Time**  
   - Serie temporale degli alert generati  

---

### 🔧 Tecnologie utilizzate

- **Python 3** 🐍  
- **PyYAML**  
- **Regex**  
- **smtplib / EmailMessage**  
- **Elasticsearch** (Docker)  
- **Grafana** (Docker)  
- **JSON, YAML**

---

### 🔜 Estensioni possibili

- Log da nginx / fail2ban / Windows Event Log  
- Export in CSV / SQLite  
- Containerizzazione + CI/CD  
- Integrazione con Prometheus e Loki
