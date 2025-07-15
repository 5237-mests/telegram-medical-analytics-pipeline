# Week 7 Final Report – Telegram-Based Medical Product Analytics Pipeline

**Name:** Mesfin Mulugeta
**Date:** July 15, 2025
**Cohort:** 10 Academy – KAIM Week 7

---

## 🧠 Project Overview

This project builds a complete data analytics pipeline for medical product insights extracted from Telegram channels. The objective is to scrape messages from various medical-related channels, extract product mentions and images, apply object detection, transform the data into a clean star schema, and expose actionable insights through an analytics API — all orchestrated via Dagster.

---

## ✅ Deliverables Summary

### 📄 Final Report & Blog Post

- ✅ This PDF report can be converted into a blog post (for Medium or similar).

### 🧭 Visual Diagrams

- ✅ End-to-end pipeline architecture diagram
- ✅ Star schema diagram showing fact and dimension tables

### 🔍 Screenshots

- ✅ API endpoints tested via Swagger UI
- ✅ Dagster pipeline executed successfully via Dagster UI
- ✅ dbt docs output visualized

### 🔗 GitHub Repository

- [https://github.com/5237-mests/telegram-medical-analytics-pipeline](https://github.com/5237-mests/telegram-medical-analytics-pipeline)

---

## 🔧 Technical Breakdown by Task

### **Task 0: Project Setup**

- Created modular Python project with `src/`, `dbt/`, `api/`, and `dagster_pipeline/`
- Set up PostgreSQL, dbt, and FastAPI

### **Task 1: Telegram Scraping**

- Used `telethon` to fetch messages
- Saved messages as JSON with media paths
- Modularized scraping logic for reuse

### **Task 2: Load to PostgreSQL & dbt Models**

- Wrote loaders for Telegram messages and YOLO results
- Created dbt staging and star schema models:

  - `stg_telegram_messages`, `fct_messages`, `dim_channels`, `dim_dates`
  - `fct_image_detections` added in Task 3

### **Task 3: YOLOv5 Integration**

- Ran object detection on images using YOLOv5
- Loaded detections to PostgreSQL
- Linked detections to messages using filename join logic

### **Task 4: Analytics API**

- Built endpoints with FastAPI:

  - `/reports/top-products`
  - `/channels/{channel}/activity`
  - `/search/messages?query=...`

- Used Pydantic for response validation
- Implemented pagination support
- Tested using Swagger UI and real queries

### **Task 5: Dagster Orchestration**

- Defined ops for each step
- Built and launched `telegram_pipeline` job
- Ran entire pipeline end-to-end from Dagster UI

---

## 🌟 Star Schema Diagram

```
+------------------+     +---------------+     +---------------------+
| dim_channels     |     | dim_dates     |     | fct_image_detections|
|------------------|     |---------------|     |---------------------|
| sender_id        |     | date_id       |     | image_file          |
| sender_name      |     | date          |     | class_name          |
+------------------+     +---------------+     | confidence          |
                                             +---------------------+
                                                |
                                                |
+--------------------------+
| fct_messages             |
|--------------------------|
| id (message_id)          |
| sender_id                |
| message_text             |
| message_date             |
| has_media, image_path    |
+--------------------------+
```

---

## 🔄 Pipeline Architecture Diagram

```
[Telegram Channels] --> [Scraper] --> [Raw JSON] --> [PostgreSQL]
                                               |
                        +--> [YOLOv5 Detection] --> [Detections]
                                               |
                            --> [dbt Transformations (star schema)]
                                               |
                            --> [FastAPI Analytics API]
                                               |
                            --> [Orchestrated with Dagster]
```

---

## 💡 Technical Choices Explained

- **Telethon** for async scraping from private/public Telegram channels
- **YOLOv5** for local image object detection (no cloud/GPU dependency)
- **PostgreSQL** as a robust structured storage layer
- **dbt** to clean and organize data into a star schema
- **FastAPI** for blazing-fast analytics API with Swagger support
- **Dagster** for declarative, modular orchestration and UI visibility

---

## 🤔 Reflections and Key Takeaways

### 🚧 Challenges

- Handling media download paths from Telegram and filename mismatches
- Matching YOLO output with original messages via filenames
- Ensuring dbt sources align correctly with raw tables
- Import path issues when launching Dagster (solved with `PYTHONPATH`)

### ✅ Key Learnings

- Power of modular pipelines (scraping, enrichment, analytics)
- Best practices in dbt modeling and schema testing
- Value of API-first design using FastAPI and Pydantic
- How orchestration tools like Dagster streamline data workflows

---

## 🎓 Outcome

- Delivered a complete, modular data analytics pipeline
- Production-ready and testable from UI (Swagger + Dagster)
- Clear code, documentation, and reusable structure

---

## 📁 Repository & Credits

- **Code**: [https://github.com/5237-mests/telegram-medical-analytics-pipeline](https://github.com/5237-mests/telegram-medical-analytics-pipeline)
- **Author**: Mesfin Mulugeta

  - 🌐 [https://www.mesfen.com](https://www.mesfen.com)
  - 💼 [LinkedIn](https://linkedin.com/in/mesfin-mulgeta) | 🧠 [GitHub](https://github.com/5237-mests)

---

**Thank you!** 🎉
