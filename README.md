# Dockerized Django REST Framework

A Django REST Framework application containerized with Docker and PostgreSQL database for development and learning purposes.

## 🚀 Quick Start

### Prerequisites

Before running this application, ensure you have the following installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:Richy-irad/drf-dockerized.git
   cd drf-dockerized
   ```

2. **Navigate to the project directory**

   ```bash
   cd drfdockerized
   ```

## 🐳 Running the Application

### First Time Setup

1. **Build the Docker images**

   ```bash
   docker-compose build
   ```

   This command builds the Docker images for your application based on the Dockerfile and docker-compose.yml configuration.

2. **Start the services**

   ```bash
   docker-compose up
   ```

   This starts both the Django web application and PostgreSQL database. The application will be available at `http://localhost:8000`.

### Subsequent Runs

For regular use after the initial setup:

```bash
docker-compose up
```

To run in detached mode (background):

```bash
docker-compose up -d
```

To stop the services:

```bash
docker-compose down
```

## 🛠️ Development Commands

### Database Operations

Run Django migrations to set up your database:

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

Create a superuser for Django admin:

```bash
docker-compose run web python manage.py createsuperuser
```

### Django Application Management

Create a new Django app:

```bash
docker-compose run web python manage.py startapp <app_name>
```

Access Django shell:

```bash
docker-compose run web python manage.py shell
```

Collect static files (for production):

```bash
docker-compose run web python manage.py collectstatic
```

### General Command Structure

To run any Django management command inside the container:

```bash
docker-compose run web python manage.py <command>
```

## 📦 Package Management

### Adding New Dependencies

1. **Add the package to requirements.txt**

   ```txt
   # Example: Adding Django REST Framework
   djangorestframework
   pytest-django
   ```

   ⚠️ **Note**: Add packages without version numbers to get the latest compatible versions.

2. **Rebuild the Docker image**

   ```bash
   docker-compose build
   ```

   This step is crucial as it installs the new packages into your Docker image.

3. **Restart the services**

   ```bash
   docker-compose up
   ```

## 🏗️ Architecture

This application uses:

- **Django REST Framework**: For building REST APIs
- **PostgreSQL**: As the database
- **Docker**: For containerization
- **Docker Compose**: For multi-container orchestration

### Services

- **web**: Django application running on port 8000
- **db**: PostgreSQL database running on port 5432

## 🤝 Contributing

1. **Adding New Services**
   - Define new services in `docker-compose.yml` under the `services` section
   - Rebuild with `docker-compose build`

2. **Database Changes**
   - Always run migrations after model changes
   - Test your changes thoroughly before committing

3. **Code Style**
   - Follow Django and Python best practices
   - Add appropriate documentation for new features

## 🐛 Troubleshooting

### Common Issues

**Port already in use:**

```bash
docker-compose down
# Wait a moment, then
docker-compose up
```

**Database connection errors:**

```bash
docker-compose down
docker-compose up
```

**Package installation issues:**

```bash
docker-compose build --no-cache
```

### Viewing Logs

To see application logs:

```bash
docker-compose logs web
```

To see database logs:

```bash
docker-compose logs db
```

## 📄 License

This project is for educational purposes.
