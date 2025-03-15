# DemoCompose

A **Docker Compose** setup for logging user signups and logins using **NGINX, Fluentd, and Django**. This project collects logs from NGINX, processes them with Fluentd, and provides an interface to manage logs.

## 🚀 Features

- **User Authentication** (Sign Up, Login)
- **NGINX as a Reverse Proxy**
- **Fluentd for Log Aggregation**
- **Docker Compose for Container Management**
- **Centralized Log Storage**

## 🛠️ Installation & Setup

### Prerequisites

Ensure you have the following installed:

- **Docker**
- **Python 3+**
- **Git**

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Naseer-010/Docker-Demo-Compose.git
   cd DemoCompose
   ```
2. **Build and start Containers**
 - In the Terminal, being in Docker-compose folder, run
   ```bash
   docker-compose up --build -d
   ```
   Note:You must have docker engine running to build the containers. You can do this just by starting the Docker Desktop app or starting it manually.
3. **Start the Django application**
   ```bash
   python manage.py runserver
   ```
4. **Access the application**
- Django App: `http://localhost:8000/home`
- Nginx Proxy: `http://localhost/home` <br>
  To ensure that nginx logs the user activity done in the application(like refreshing the page accessing different URL) use nginx proxied server URL.
5. **Check the logs**
- Nginx logs are stored in "./nginx/logs" folder.
- To collect the logs via Fluentd and save them in a output file, run `docker restart fluentd` in the terminal.
    - This will ensure fluentd will collect the logs and save them into an output file.
    - Find fluentd processed logs in "./fluentd/output_logs" folder
  













