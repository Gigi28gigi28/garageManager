# Garage Repair Management System with RabbitMQ

A microservices-based garage management system demonstrating asynchronous message processing using RabbitMQ, Django REST Framework, and Python.

## Overview

This system showcases a message-driven architecture for handling car repair requests. It uses RabbitMQ as a message broker to decouple the repair request service from the repair processing service, enabling asynchronous, reliable, and scalable operations.

##  System Architecture

```
Client Request → Django Service → RabbitMQ Queue → Consumer → Django API
```

**Components:**
1. **Producer Service** (`service/`) - Receives repair requests and publishes to RabbitMQ
2. **RabbitMQ** - Message broker queue (`garage` queue)
3. **Consumer** (`consomateur.py`) - Processes messages and creates repair records
4. **REST API** (`metier/`) - Manages pieces and repairs in the database

##  Features

- **Asynchronous Processing** - Non-blocking repair request handling
- **Message Queuing** - Reliable message delivery with RabbitMQ
- **RESTful API** - Full CRUD operations for parts and repairs
- **Durable Queues** - Messages persist even if broker restarts
- **Manual Acknowledgment** - Ensures message processing reliability
- **Django Admin** - Built-in administration interface

##  Tech Stack

- **Backend Framework:** Django 5.1.7
- **API:** Django REST Framework
- **Message Broker:** RabbitMQ (via Pika)
- **Database:** SQLite (easily replaceable with PostgreSQL/MySQL)
- **Python:** 3.x

##  Project Structure

```
garage-repair-rabbitmq/
├── metier/                 # Business logic app
│   ├── models.py          # Piece, Reparation, Voiture models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API ViewSets
│   └── urls.py            # API endpoints
├── service/               # Service layer
│   ├── views.py          # Repair request handler
│   └── apps.py           # RabbitMQ queue initialization
├── rabbitmq/             # Django project settings
├── consomateur.py        # RabbitMQ consumer
└── manage.py             # Django management script
```

## Database Models

### Piece (Auto Part)
- `nom` - Part name
- `prix` - Price

### Reparation (Repair)
- `piece` - Foreign key to Piece
- `duree` - Duration in hours

### Voiture (Car)
- `marque` - Brand/Make
- `couleur` - Color

##  Getting Started

### Prerequisites

- Python 3.8+
- RabbitMQ server
- pip

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd garage-repair-rabbitmq
```

2. **Install Python dependencies**
```bash
pip install django djangorestframework pika requests
```

3. **Install RabbitMQ**

**Ubuntu/Debian:**
```bash
sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server
```

**macOS:**
```bash
brew install rabbitmq
brew services start rabbitmq
```

**Windows:**
Download and install from [RabbitMQ official website](https://www.rabbitmq.com/download.html)

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

### Running the Application

1. **Start Django server**
```bash
python manage.py runserver
```

2. **Start RabbitMQ consumer** (in another terminal)
```bash
python consomateur.py
```

##  API Endpoints

### REST API Endpoints

**Pieces (Auto Parts)**
- `GET /api/piece/` - List all parts
- `POST /api/piece/` - Create a part
- `GET /api/piece/{id}/` - Get part details
- `PUT /api/piece/{id}/` - Update part
- `DELETE /api/piece/{id}/` - Delete part

**Reparations (Repairs)**
- `GET /api/reparation/` - List all repairs
- `POST /api/reparation/` - Create a repair
- `GET /api/reparation/{id}/` - Get repair details
- `PUT /api/reparation/{id}/` - Update repair
- `DELETE /api/reparation/{id}/` - Delete repair

### Service Endpoints

**Repair Request**
- `GET /reparation/{piece_id}/{duree}/` - Submit repair request

##  Message Flow

1. **Client requests repair:**
   ```
   GET /reparation/1/5/
   ```

2. **Service publishes to RabbitMQ:**
   ```json
   {"piece": 1, "duree": 5}
   ```

3. **Consumer receives message:**
   - Decodes message from queue
   - Posts to REST API
   - Acknowledges message on success

4. **API creates repair record:**
   - Stores in database
   - Returns success response

##  Testing the System

### 1. Create a Part
```bash
curl -X POST http://localhost:8000/api/piece/ \
  -H "Content-Type: application/json" \
  -d '{"nom": "Brake Pads", "prix": 50.00}'
```

### 2. Request Repair
```bash
curl http://localhost:8000/reparation/1/3/
```

### 3. Check Queue (RabbitMQ Management UI)
```
http://localhost:15672
Username: guest
Password: guest
```

### 4. Verify Repair Created
```bash
curl http://localhost:8000/api/reparation/
```

##  Configuration

### RabbitMQ Connection
Edit connection parameters in `consomateur.py` and `service/views.py`:
```python
pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials('username', 'password')
)
```

### Queue Settings
Modify in `service/apps.py`:
```python
ch.queue_declare(queue="garage", durable=True)
```

