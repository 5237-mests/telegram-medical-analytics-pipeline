import os

# Define folder structure
folders = [
    "data/raw/telegram_messages",
    "src",
    "dbt/medigram_dbt",
    "dagster_project"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create essential files
files = [
    ".env",
    ".gitignore",
    "README.md",
    "docker-compose.yml",
    "Dockerfile",
    "requirements.txt",
    "src/__init__.py",
    "src/main.py",
    "src/database.py",
    "src/models.py",
    "src/schemas.py",
    "src/crud.py",
    "src/telegram_scraper.py"
]

for file in files:
    with open(file, 'w') as f:
        pass  # Create empty file

print("✅ Project structure created successfully!")
