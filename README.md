# Football Trivia

A Django web application for football trivia quizzes and polls. Users can register, log in, participate in polls, and view trivia content.

---

## Features

- User registration and authentication
- Secure login and logout
- Polls with voting restricted to logged-in users
- Trivia questions and answers display
- Docker support for containerized deployment
- Sphinx-generated documentation for the codebase

---

## Project Structure

- `football_trivia/` - Django project root
- `blog/` - Blog/trivia app
- `authentication/` - User auth app
- `docs/` - Sphinx documentation source (on `docs` branch)
- `Dockerfile`, `docker-compose.yml` - Docker container setup (on `container` branch)
- `db.sqlite3` - SQLite database file (optional, see notes)

---

## Getting Started

### Prerequisites

- Python 3.12+
- pip
- (Optional) Docker and Docker Compose

---


### 🧪 Local Development Setup
1. Clone the repo:
```bash
git clone https://github.com/prestonreddi/football_trivia.git
cd football_trivia