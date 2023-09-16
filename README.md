# LangChain LLM Model

## Introduction
This Django project demonstrates how to create a custom user model and define related models for user profiles, PDF documents, and chat messages.

## Features
- **Advanced Chatbot Integration**: Utilizes cutting-edge Generative AI and advanced language models to power a chatbot that enables users to interact with uploaded PDF documents.
- **PDF Document Upload**: Allows users to upload PDF files, making them accessible for content-based queries.
- **Real-time Responses**: Provides real-time chatbot responses to user queries about the content of uploaded PDF documents.
- **Responsive UI**: Implements a responsive user interface, ensuring a seamless experience across various devices for enhanced accessibility.
- **Chat History**: Designed and implemented a chat history feature, allowing users to revisit previous conversations with the chatbot, fostering a user-friendly interaction.
- **Technology Stack**: Employed Python, Django, PyPDF2, chatbot frameworks, LLM, openAI, and natural language processing libraries to architect and develop this solo project, demonstrating proficiency in these industry-standard technologies.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python (3.x) installed on your system.
- Django installed (`pip install Django`).
- Langchain library installed (`pip install langchain`).
- PyPDF2 library installed (`pip install PyPDF2`).
- OpenAI API key (set it as an environment variable named `OPENAI_API_KEY`).



## Getting Started
### Installation & Getting started
Detailed instructions on how to install, configure, and get the project running:

1. Clone the repository: `git clone https://github.com/amanastel/llm_project.git`
2. Navigate to the project directory: `cd PDF_Based_Chatbot_AI`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`

## APIs Used
1. Create a superuser to access the admin panel: `python manage.py createsuperuser`
2. Start the development server: `python manage.py runserver`
3. Access the admin panel at: `http://localhost:8000/admin/`
4. Use the admin panel to manage users, profiles, PDF documents, and chat messages.

## API Endpoints
- User Registration: `POST /api/register/`
- User Login: `POST /api/login/`
- User Profile: `GET /api/profile/`
- Upload PDF Document: `POST /api/upload-pdf/`
- List PDF Documents: `GET /api/pdf-documents/`
- Create Chat Message: `POST /api/chat/create/`
- List Chat Messages: `GET /api/chat/list/`

## Custom User Serializer
You can find the `CustomUserSerializer` in the `serializers.py` file under the `llmApp` app directory. This serializer is used for user registration and login.

## Models
- `CustomProfile`: Represents user profiles with extended fields (phone and address).
- `PDFDocument`: Represents uploaded PDF documents associated with users.
- `ChatMessage`: Represents chat messages with timestamps.

## Technology Stack
- Django
- Python
- Langchain
- MySQL
- Vue

## Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
