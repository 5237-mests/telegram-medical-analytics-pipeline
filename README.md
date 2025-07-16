### ✅ `README.md`

# 🧪 Telegram Medical Analytics Pipeline

An end-to-end data pipeline that scrapes Telegram medical channels, detects products using YOLO, models data using dbt, serves insights via FastAPI, and orchestrates the whole process with Dagster.

## 📦 Features

- Scrapes messages and images from Telegram channels
- Applies YOLOv5 for product detection in images
- Loads raw and enriched data to PostgreSQL
- Transforms data into a star schema using dbt
- Serves business-focused analytics through FastAPI
- Fully orchestrated using Dagster with visual UI

---

## 🛠️ Tech Stack

| Layer          | Tools Used            |
| -------------- | --------------------- |
| Scraping       | `telethon`            |
| Detection      | `YOLOv5`              |
| Storage        | `PostgreSQL`          |
| Transformation | `dbt`                 |
| API            | `FastAPI`, `Pydantic` |
| Orchestration  | `Dagster`             |

---

## 📊 Star Schema Overview

dim_channels dim_dates fct_image_detections
+-----------+ +---------+ +--------------------+
|sender_id | |date_id | |image_file |
|name | |date | |class_name |
+-----------+ +---------+ |confidence |
+--------------------+
|
|
+------------------+--------------------+
\| fct_messages |
+----------------------------------------+
\| message_id | sender_id | has_media ...|
+----------------------------------------+

---

## 📈 Key API Endpoints

- `GET /api/reports/top-products?limit=10`
- `GET /api/channels/{channel_name}/activity`
- `GET /api/search/messages?query=...`
- `GET /api/health`

Testable via Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚀 How to Run

### 1. Clone & Setup

```
git clone https://github.com/5237-mests/telegram-medical-analytics-pipeline.git
cd telegram-medical-analytics-pipeline
python -m venv week7
source week7/bin/activate  # or week7\\Scripts\\activate on Windows
pip install -r requirements.txt
```

### 2. Environment Setup

Create a `.env` file at root:

```
TELEGRAM_API_ID=...
TELEGRAM_API_HASH=...
POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_HOST=...
POSTGRES_PORT=5432
PYTHONPATH=.
```

### 3. Run the Pipeline (Dagster UI)

```
dagster dev --workspace dagster_pipeline/workspace.yaml
# Open: http://localhost:3000
```

### 4. Run the API Server

```bash
uvicorn api.main:app --reload
# Open: http://localhost:8000/docs
```

---

## 🖼️ Screenshots

> 📌 See `/screenshots` folder for:

- API tested via Swagger
- dbt docs UI
- Dagster pipeline UI
- Telegram scrape samples

---

## 🐳 Docker Setup

This project supports containerized development using **Docker** and **Docker Compose**. Follow these steps to run the full pipeline including FastAPI, PostgreSQL, and Dagster.

### 📦 Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 🚀 Running the Project

1. **Clone the repository** (if not already):

   ```bash
   git clone https://github.com/your-username/telegram-medical-analytics-pipeline.git
   cd telegram-medical-analytics-pipeline
   ```

2. **Set up environment variables**
   Create a `.env` file in the root directory with the following variables:

   ```env
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=medigram
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432

   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```

3. **Build and run all containers**

   ```bash
   docker-compose build
   docker-compose up
   ```

---

### 🧪 Available Services

| Service    | URL                                                      | Description                      |
| ---------- | -------------------------------------------------------- | -------------------------------- |
| FastAPI    | [http://localhost:8000/docs](http://localhost:8000/docs) | API with analytics endpoints     |
| PostgreSQL | localhost:5432                                           | Database for storing messages    |
| Dagster UI | [http://localhost:3000](http://localhost:3000)           | Orchestrate and monitor pipeline |

---

### 🛑 Stopping the Containers

To shut everything down:

```bash
docker-compose down
```

---

## 🧠 Author

**Mesfin Mulugeta Wetere**
💼 [LinkedIn](https://linkedin.com/in/mesfin-mulgeta)
🐙 [GitHub](https://github.com/5237-mests)

---

## 🌟 Acknowledgments

Built as part of **10 Academy KAIM Week 7** project.
