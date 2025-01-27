# ResumeAlign

ResumeAlign is a powerful web application that helps users optimize their resumes for specific job descriptions using AI. The app analyzes job descriptions and existing resumes, then generates tailored, ATS-friendly resumes that highlight relevant skills and experiences.

## Features

- **AI-Powered Resume Optimization**: Automatically align your resume with job descriptions using Claude AI
- **Profile Management**: Maintain and update your professional profile, including work experience, education, skills, and projects
- **Custom Resume Generation**: Generate targeted resumes based on your profile and specific job descriptions
- **PDF Export**: Export your optimized resume in beautifully formatted PDF
- **Modern UI**: Clean, responsive interface built with Tailwind CSS

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Database**: TinyDB
- **AI**: Claude API (Anthropic)
- **PDF Generation**: WeasyPrint
- **Template Engine**: Jinja2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/FayazK/ResumeAlign.git
cd ResumeAlign
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Development

Start the development server:
```bash
uvicorn app.main:app --reload
```


The application will be available at `http://localhost:8000`

## Project Structure

```
resume_app/
├── app/
│   ├── main.py           # FastAPI application
│   ├── models.py         # Database models
│   ├── routers/          # API routes
│   └── services/         # Business logic
├── static/               # Static files
├── templates/            # HTML templates
├── tests/                # Test files
└── requirements.txt      # Python dependencies
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Anthropic](https://www.anthropic.com/)
- [WeasyPrint](https://weasyprint.org/)