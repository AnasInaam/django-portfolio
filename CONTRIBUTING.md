# Contributing to Django Portfolio

Thank you for your interest in contributing to this Django Portfolio project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- Check existing issues before creating a new one
- Use clear, descriptive titles
- Include steps to reproduce the issue
- Provide environment details (OS, Python version, Django version)
- Add screenshots if applicable

### Suggesting Features
- Open an issue with the "feature request" label
- Describe the feature and its benefits
- Provide examples or mockups if possible
- Discuss implementation approaches

### Code Contributions

#### Prerequisites
- Python 3.8 or higher
- Django 5.1.2
- Git knowledge
- Basic understanding of HTML, CSS, JavaScript

#### Development Setup
1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/django-portfolio.git
   cd django-portfolio
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Load sample data:
   ```bash
   python manage.py populate_data
   ```

#### Making Changes
1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes following the coding standards
3. Test your changes thoroughly
4. Commit with clear, descriptive messages:
   ```bash
   git commit -m "Add: Feature description"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Create a Pull Request

## 📋 Coding Standards

### Python/Django Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Use Django best practices

### HTML/CSS/JavaScript
- Use semantic HTML5 elements
- Follow Bootstrap 5 conventions
- Keep CSS organized and commented
- Use ES6+ JavaScript features
- Ensure cross-browser compatibility

### Database
- Write descriptive migration files
- Use appropriate field types
- Add helpful verbose names and help text
- Consider database performance

## 🧪 Testing

### Running Tests
```bash
python manage.py test
```

### Test Coverage
- Write tests for new features
- Ensure existing tests pass
- Test both positive and negative scenarios
- Include edge cases

### Manual Testing
- Test on different screen sizes
- Verify dark/light theme functionality
- Check form validation
- Test navigation and user flows

## 📝 Pull Request Guidelines

### Before Submitting
- [ ] Code follows project standards
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Screenshots included for UI changes
- [ ] Performance impact considered

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] All tests pass
- [ ] Tested on multiple browsers/devices

## Screenshots (if applicable)
[Add screenshots here]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 🏗️ Project Structure

```
django-portfolio/
├── portfolio/              # Main Django app
├── portfolio_site/         # Project settings
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploaded files
├── requirements.txt        # Python dependencies
└── manage.py              # Django management script
```

## 🎯 Areas for Contribution

### High Priority
- Performance optimizations
- Accessibility improvements
- Mobile responsiveness enhancements
- SEO optimizations

### Medium Priority
- Additional project templates
- Enhanced admin interface
- Blog functionality
- API endpoints

### Low Priority
- Multi-language support
- Advanced analytics
- Social media integrations
- Third-party service integrations

## 📖 Resources

### Django Documentation
- [Django Official Docs](https://docs.djangoproject.com/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

### Frontend Resources
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [MDN Web Docs](https://developer.mozilla.org/)

## 💬 Communication

### Getting Help
- Open an issue for questions
- Join discussions in existing issues
- Check the documentation first

### Code Review Process
- All submissions require review
- Feedback is provided constructively
- Changes may be requested before merging
- Maintainers have final approval

## 🏆 Recognition

Contributors will be recognized in:
- GitHub contributors list
- Project documentation
- Release notes
- Special thanks section

## 📜 Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors:

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

## 📞 Contact

**Project Maintainer**: Anas Inaam
- GitHub: [@AnasInaam](https://github.com/AnasInaam)
- Email: anas.inaam@example.com

---

Thank you for contributing to making this portfolio project better! 🚀
