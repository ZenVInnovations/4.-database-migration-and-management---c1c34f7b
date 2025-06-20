# Database Migration and Management

This repository demonstrates how to set up and manage database migrations in a Python project using Alembic, with a structured project layout. It also includes configurations and migration scripts necessary for effective database version control.

## 📁 Project Structure

├── alembic/ # Alembic migration environment

├── config/ # Configuration files (DB URI, settings, etc.)

├── core/ # Core logic (models, database setup, etc.)

├── migrations/ # Alembic-generated migration scripts

├── alembic.ini # Alembic configuration file

├── main.py # Entry point or sample execution script

├── requirements.txt # List of Python dependencies


## ⚙️ Features

- Alembic for version-controlled database migrations
- Clean project structure for scalability
- Environment-based configuration support
- Easy integration with SQLAlchemy

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ZenVInnovations/4.-database-migration-and-management---c1c34f7b.git
cd 4.-database-migration-and-management---c1c34f7b
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies

```
pip install -r requirements.txt

```

### 4. Run Alembic Migrations
Initialize and upgrade your database schema:
```
alembic upgrade head

```
To create a new migration after modifying models:
```
alembic revision --autogenerate -m "Your message"
alembic upgrade head

```
### 5. Run the Application
```
python main.py

```
