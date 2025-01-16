## Services

### Service 1

- **Path:** `service1/app.py`
- **Description:** This service exposes an API endpoint `/api/message` which fetches a message from Service 2.
- **Port:** 5000

### Service 2

- **Path:** `service2/app.py`
- **Description:** This service exposes an API endpoint `/api/get-string` which retrieves a message from the PostgreSQL database.
- **Port:** 5001

### PostgreSQL

- **Path:** `postgres/init.sql`
- **Description:** Initializes the database with a `messages` table and inserts a sample message.
- **Port:** 5432

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository.
2. Navigate to the project directory.
3. Run the following command to start the services:

    ```sh
    docker-compose up --build
    ```

4. Access the services:
    - Service 1: `http://localhost:5000/api/message`
    - Service 2: `http://localhost:5001/api/get-string`

### Stopping the Application

To stop the services, run:

```sh
docker-compose down