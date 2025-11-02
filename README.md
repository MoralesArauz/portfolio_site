# Flask Portfolio Website

This is a personal portfolio website built with Flask to showcase my Python projects, web development skills, and data visualizations. It includes a dynamic project gallery, a contact form with email integration, and a clean Bootstrap-based design.

## 🔧 Features

- 🖼️ Project gallery powered by JSON
- 📬 Contact form with email sending via SMTP
- 🎨 Responsive layout using Bootstrap 5
- 🧠 Modular Flask architecture for scalability
- 📊 Ready for data visualizations with matplotlib or Plotly
- 🔒 Environment variable support for secure credentials

## 📁 Project Structure

```
portfolio_site/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/style.css
│   │   └── images/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── projects.html
│       └── contact.html
├── projects.json
├── config.py
├── requirements.txt
├── .env
└── run.py
```

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/flask-portfolio.git
   cd flask-portfolio
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   SECRET_KEY=your_secret_key
   ```

5. Run the app:
   ```bash
   python run.py
   ```

## 📬 Contact

Feel free to reach out via the contact form on the site or connect with me on [LinkedIn](https://www.linkedin.com/in/adri%C3%A1n-morales-a951b5124/) or [GitHub](https://github.com/MoralesArauz).
```

Let me know if you want to add a screenshot, deployment instructions, or badges for Python version and license.
