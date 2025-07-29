⚽ Football Trivia
A Django-based web application for football trivia quizzes and polls. Users can register, log in, participate in polls, and read trivia content. The project includes Docker support for containerized deployment and developer documentation generated with Sphinx.

🚀 Features
User registration and authentication system
Football trivia polls and voting (only for logged-in users)
Trivia blog-like content
Docker support for easy deployment
Developer documentation generated with Sphinx

📋 What to Expect
After setup, users will be able to:
Register and log into their accounts
Browse trivia polls and vote
Read football-related trivia articles and quizzes
Interact with content in a clean and responsive interface


🛠️ Local Setup Instructions
1. Clone the repository
git clone https://github.com/prestonreddi/football_trivia.git
cd football_trivia

2. Set up a virtual environment
python -m venv env

Activate the virtual environment:
Windows:
.\env\Scripts\activate
macOS/Linux:
source env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create a .env file in the root directory with the following content:

DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

5. Apply migrations
python manage.py migrate

6. Create a superuser
python manage.py createsuperuser

7. Run the development server
python manage.py runserver
Visit the app at: http://localhost:8000

🐳 Docker Setup 
You can also run the app using Docker:

1. Build the Docker image
docker build -t football_trivia .

2. Run the container
docker run -d -p 8000:8000 football_trivia
Visit: http://localhost:8000


🧩 How to Use the Application
Register: Create a new user account
Login: Access your account using your credentials
Polls: Browse trivia questions and cast your vote (authentication required)
Trivia Blog: Read through football-related facts and content
Logout: Securely sign out

🧑‍💻 Developer Documentation 
This project includes developer documentation built using Sphinx.

1. Ensure dependencies are installed
pip install -r requirements.txt

2. Navigate to the docs directory
cd docs

3. Build the HTML documentation
make html

4. Open the documentation
Windows: Open _build\html\index.html in your browser

macOS/Linux: Open _build/html/index.html in your browser


👤 Author
Preston Reddi
GitHub: prestonreddi