from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import Profile, Skill, Project, Experience, Education, Contact
from django.utils import timezone
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample portfolio data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to populate database with sample data...'))

        # Create or get superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@portfolio.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created superuser: admin/admin123'))

        # Create Profile
        profile, created = Profile.objects.get_or_create(
            name="John Doe",
            defaults={
                'title': "Full Stack Developer",
                'bio': "Passionate full-stack developer with 5+ years of experience in creating robust web applications. Specialized in Python, Django, React, and modern web technologies. Love turning complex problems into simple, beautiful solutions.",
                'email': "john.doe@example.com",
                'phone': "+1 (555) 123-4567",
                'location': "San Francisco, CA",
                'linkedin_url': "https://linkedin.com/in/johndoe",
                'github_url': "https://github.com/johndoe",
                'twitter_url': "https://twitter.com/johndoe",
                'website_url': "https://johndoe.dev",
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created profile for John Doe'))

        # Create Technologies (Skills)
        skills_data = [
            {'name': 'Python', 'category': 'backend', 'proficiency': 95, 'icon': 'fab fa-python'},
            {'name': 'Django', 'category': 'backend', 'proficiency': 90, 'icon': 'fas fa-server'},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 88, 'icon': 'fab fa-js'},
            {'name': 'React', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-react'},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 95, 'icon': 'fab fa-html5'},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 90, 'icon': 'fab fa-css3-alt'},
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-database'},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 75, 'icon': 'fab fa-docker'},
            {'name': 'Git', 'category': 'tools', 'proficiency': 90, 'icon': 'fab fa-git-alt'},
            {'name': 'AWS', 'category': 'tools', 'proficiency': 70, 'icon': 'fab fa-aws'},
            {'name': 'Node.js', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-node-js'},
            {'name': 'Bootstrap', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-bootstrap'},
        ]

        skills = {}
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            skills[skill_data['name']] = skill
            if created:
                self.stdout.write(f'Created skill: {skill_data["name"]}')

        # Create Additional Skills
        additional_skills_data = [
            {'name': 'Web Development', 'category': 'other', 'proficiency': 95},
            {'name': 'Database Design', 'category': 'database', 'proficiency': 85},
            {'name': 'API Development', 'category': 'backend', 'proficiency': 90},
            {'name': 'Project Management', 'category': 'other', 'proficiency': 80},
            {'name': 'Team Leadership', 'category': 'other', 'proficiency': 85},
            {'name': 'Problem Solving', 'category': 'other', 'proficiency': 95},
            {'name': 'Communication', 'category': 'other', 'proficiency': 90},
            {'name': 'Agile/Scrum', 'category': 'other', 'proficiency': 85},
        ]

        for skill_data in additional_skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill_data["name"]}')

        # Create Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'short_description': 'A full-featured e-commerce platform built with Django and React',
                'description': '''A comprehensive e-commerce solution featuring:
                
• User authentication and profile management
• Product catalog with advanced filtering
• Shopping cart and checkout process
• Payment integration with Stripe
• Order tracking and management
• Admin dashboard for inventory management
• Responsive design for all devices
• RESTful API for mobile app integration

Built using Django REST Framework for the backend API, React for the frontend, PostgreSQL for data storage, and deployed on AWS with Docker containers.''',
                'technologies': ['Python', 'Django', 'React', 'PostgreSQL', 'AWS'],
                'github_url': 'https://github.com/johndoe/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.johndoe.dev',
                'featured': True,
                'created_date': date.today() - timedelta(days=180)
            },
            {
                'title': 'Task Management App',
                'short_description': 'A collaborative task management application with real-time updates',
                'description': '''A modern task management application that helps teams collaborate effectively:

• Real-time task updates using WebSockets
• Project organization and team management
• Time tracking and reporting features
• File attachments and comments
• Mobile-responsive design
• Integration with popular tools like Slack and GitHub
• Advanced filtering and search capabilities
• Customizable dashboards and notifications

Developed with Django Channels for real-time features, Vue.js for the frontend, and Redis for caching and WebSocket support.''',
                'technologies': ['Python', 'Django', 'JavaScript', 'PostgreSQL', 'Docker'],
                'github_url': 'https://github.com/johndoe/task-manager',
                'live_url': 'https://taskapp.johndoe.dev',
                'featured': True,
                'created_date': date.today() - timedelta(days=120)
            },
            {
                'title': 'Portfolio Website',
                'short_description': 'Personal portfolio website with modern design and animations',
                'description': '''A sleek and modern portfolio website showcasing:

• Responsive design with smooth animations
• Dark/light theme toggle
• Project showcase with filtering
• Contact form with email integration
• SEO optimized with meta tags
• Fast loading with optimized images
• Cross-browser compatibility
• Accessibility features

Built with Django for the backend, modern CSS with animations, and deployed on a cloud platform for optimal performance.''',
                'technologies': ['Django', 'HTML5', 'CSS3', 'JavaScript', 'Bootstrap'],
                'github_url': 'https://github.com/johndoe/portfolio',
                'live_url': 'https://johndoe.dev',
                'featured': False,
                'created_date': date.today() - timedelta(days=60)
            },
            {
                'title': 'Weather Dashboard',
                'short_description': 'Interactive weather dashboard with data visualization',
                'description': '''An interactive weather dashboard providing:

• Current weather conditions for multiple cities
• 7-day weather forecast with detailed information
• Interactive maps with weather overlays
• Historical weather data and trends
• Weather alerts and notifications
• Customizable dashboard widgets
• Data export functionality
• Mobile app companion

Integrated with multiple weather APIs for accurate data, featuring charts and graphs for data visualization, and includes geolocation support.''',
                'technologies': ['React', 'Node.js', 'JavaScript', 'CSS3'],
                'github_url': 'https://github.com/johndoe/weather-dashboard',
                'live_url': 'https://weather.johndoe.dev',
                'featured': False,
                'created_date': date.today() - timedelta(days=90)
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'short_description': project_data['short_description'],
                    'description': project_data['description'],
                    'github_url': project_data['github_url'],
                    'live_url': project_data['live_url'],
                    'featured': project_data['featured'],
                    'created_date': project_data['created_date']
                }
            )
            
            if created:
                # Add technologies to project
                for tech_name in project_data['technologies']:
                    if tech_name in skills:
                        project.technologies.add(skills[tech_name])
                self.stdout.write(f'Created project: {project_data["title"]}')

        # Create Experience
        experiences_data = [
            {
                'company': 'TechCorp Solutions',
                'position': 'Senior Full Stack Developer',
                'description': '''Leading development of enterprise web applications and mentoring junior developers.

Key Responsibilities:
• Architected and developed scalable web applications using Django and React
• Led a team of 4 developers in agile development practices
• Implemented CI/CD pipelines reducing deployment time by 60%
• Collaborated with product managers and designers on user experience
• Conducted code reviews and established coding standards
• Mentored junior developers and interns

Notable Achievements:
• Improved application performance by 40% through optimization
• Successfully delivered 5 major projects on time and under budget
• Implemented automated testing increasing code coverage to 95%''',
                'start_date': date(2022, 1, 1),
                'end_date': None,
                'location': 'San Francisco, CA'
            },
            {
                'company': 'StartupXYZ',
                'position': 'Full Stack Developer',
                'description': '''Developed and maintained web applications for a fast-growing startup.

Key Responsibilities:
• Built responsive web applications using Python, Django, and JavaScript
• Integrated third-party APIs and payment systems
• Optimized database queries and application performance
• Collaborated in cross-functional teams using Agile methodologies
• Participated in product planning and technical decision making

Achievements:
• Reduced page load times by 50% through code optimization
• Implemented new features that increased user engagement by 30%
• Contributed to successful Series A funding round through product development''',
                'start_date': date(2020, 6, 1),
                'end_date': date(2021, 12, 31),
                'location': 'San Francisco, CA'
            },
            {
                'company': 'WebDev Agency',
                'position': 'Junior Web Developer',
                'description': '''Started career as a junior developer working on various client projects.

Key Responsibilities:
• Developed websites and web applications for small to medium businesses
• Worked with HTML, CSS, JavaScript, and PHP
• Collaborated with designers to implement pixel-perfect designs
• Maintained and updated existing client websites
• Provided technical support and training to clients

Learning Experience:
• Gained experience in project management and client communication
• Learned industry best practices and coding standards
• Developed skills in responsive design and cross-browser compatibility''',
                'start_date': date(2019, 3, 1),
                'end_date': date(2020, 5, 31),
                'location': 'San Jose, CA'
            }
        ]

        for exp_data in experiences_data:
            exp, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {exp_data["position"]} at {exp_data["company"]}')

        # Create Education
        education_data = [
            {
                'institution': 'University of California, Berkeley',
                'degree': 'Bachelor of Science',
                'field_of_study': 'Computer Science',
                'description': '''Comprehensive computer science education covering:

Core Subjects:
• Data Structures and Algorithms
• Software Engineering Principles
• Database Systems
• Computer Networks
• Operating Systems
• Web Development
• Machine Learning Fundamentals

Projects and Activities:
• Developed a social media platform as capstone project
• Participated in ACM programming competitions
• Teaching assistant for Introduction to Programming course
• Member of Computer Science Student Association

GPA: 3.8/4.0 - Graduated Magna Cum Laude''',
                'start_date': date(2015, 8, 1),
                'end_date': date(2019, 5, 31),
                'gpa': '3.8'
            },
            {
                'institution': 'FreeCodeCamp',
                'degree': 'Full Stack Web Development',
                'field_of_study': 'Web Development',
                'description': '''Completed comprehensive full-stack web development curriculum:

Certifications Earned:
• Responsive Web Design
• JavaScript Algorithms and Data Structures
• Front End Development Libraries
• Data Visualization
• Back End Development and APIs
• Quality Assurance

Projects Completed:
• Built 15+ responsive websites and web applications
• Developed RESTful APIs and microservices
• Created data visualization dashboards
• Implemented automated testing suites''',
                'start_date': date(2018, 6, 1),
                'end_date': date(2019, 2, 28),
                'gpa': ''
            }
        ]

        for edu_data in education_data:
            edu, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                field_of_study=edu_data['field_of_study'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {edu_data["degree"]} from {edu_data["institution"]}')

        # Create some sample contact messages (without created_at since it's auto-generated)
        contact_messages = [
            {
                'name': 'Alice Johnson',
                'email': 'alice@example.com',
                'subject': 'Project Inquiry',
                'message': 'Hi John, I saw your portfolio and I\'m interested in discussing a web development project for my startup. Would you be available for a call this week?',
            },
            {
                'name': 'Bob Smith',
                'email': 'bob@techcompany.com',
                'subject': 'Job Opportunity',
                'message': 'Hello John, we have an exciting senior developer position that might interest you. Your experience with Django and React aligns perfectly with what we\'re looking for.',
            },
            {
                'name': 'Carol Davis',
                'email': 'carol@design.studio',
                'subject': 'Collaboration',
                'message': 'Hi John, I\'m a UI/UX designer and I\'d love to collaborate on some projects. Your development skills combined with my design expertise could create amazing results!',
            }
        ]

        for contact_data in contact_messages:
            contact, created = Contact.objects.get_or_create(
                email=contact_data['email'],
                subject=contact_data['subject'],
                defaults=contact_data
            )
            if created:
                self.stdout.write(f'Created contact message from: {contact_data["name"]}')

        self.stdout.write(
            self.style.SUCCESS(
                '\n✅ Database populated successfully with sample data!\n'
                '\nYou can now:\n'
                '1. Visit http://127.0.0.1:8000/ to see your portfolio\n'
                '2. Login to admin at http://127.0.0.1:8000/admin/ with:\n'
                '   Username: admin\n'
                '   Password: admin123\n'
                '3. Add your own content and customize the portfolio\n'
            )
        )
