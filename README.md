#  Django Portfolio Website

A modern, responsive portfolio website built with Django, Bootstrap 5, and modern web technologies. Perfect for showcasing your projects, skills, and professional experience.

![Django](https://img.shields.io/badge/Django-5.1.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13.7-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

##  Features

###  Modern Design
- **Responsive Layout**: Fully responsive design that works on all devices
- **Dark/Light Theme**: Toggle between dark and light modes with smooth transitions
- **Smooth Animations**: CSS animations and transitions for enhanced user experience
- **Professional UI**: Clean, modern interface using Bootstrap 5.3.2

###  Core Functionality
- **Home Page**: Hero section with dynamic content and social links
- **About Page**: Detailed information about skills, experience, and background
- **Projects Portfolio**: Showcase your projects with images, descriptions, and live links
- **Contact Form**: Functional contact form with validation and email notifications
- **Admin Panel**: Django admin interface for easy content management

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   `ash
   git clone https://github.com/AnasInaam/django-portfolio.git
   cd django-portfolio
   `

2. **Create virtual environment**
   `ash
   python -m venv .venv
   `

3. **Activate virtual environment**
   - Windows: .venv\Scripts\activate
   - macOS/Linux: source .venv/bin/activate

4. **Install dependencies**
   `ash
   pip install -r requirements.txt
   `

5. **Run migrations**
   `ash
   python manage.py migrate
   `

6. **Create superuser**
   `ash
   python manage.py createsuperuser
   `

7. **Run the development server**
   `ash
   python manage.py runserver
   `

8. **Open your browser**
   - Portfolio: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

##  Technology Stack

### Backend
- **Django 5.1.2**: Web framework
- **Python 3.13.7**: Programming language
- **SQLite**: Database (default, easily configurable)

### Frontend
- **Bootstrap 5.3.2**: CSS framework
- **JavaScript ES6+**: Client-side functionality
- **Font Awesome 6.5.0**: Icons
- **Google Fonts**: Typography
- **CSS3**: Custom styling and animations

##  Pages Overview

###  Home Page
- Hero section with introduction
- Dynamic profile information
- Call-to-action buttons
- Social media links

###  About Page
- Detailed biography
- Skills and technologies
- Professional experience

###  Projects Page
- Project showcase with filtering
- Project details with images
- Live demo and source code links

###  Contact Page
- Contact form with validation
- Contact information display
- Social media links
- FAQ section

##  Deployment

### Production Checklist
- [ ] Set DEBUG = False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up production database
- [ ] Configure static files serving
- [ ] Set up email backend
- [ ] Configure domain and SSL

### Popular Deployment Options
- **Heroku**: Easy deployment with Git
- **DigitalOcean**: VPS hosting
- **AWS**: Scalable cloud hosting
- **PythonAnywhere**: Python-specific hosting

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with  using Django & Bootstrap**

*Happy coding! *
