from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Proficiency level (0-100)")
    category = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Technologies'),
        ('other', 'Other'),
    ])
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class for icon (e.g., fab fa-python)")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-proficiency', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Skill, blank=True)
    github_url = models.URLField(blank=True, validators=[URLValidator()])
    live_url = models.URLField(blank=True, validators=[URLValidator()])
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    
    # Additional fields from migration
    bookmarks = models.PositiveIntegerField(default=0)
    challenges = models.TextField(blank=True, help_text='Key challenges faced and solutions')
    demo_available = models.BooleanField(default=False)
    duration = models.CharField(max_length=50, blank=True, help_text='e.g., 3 months, 2 weeks')
    learned = models.TextField(blank=True, help_text='What was learned from this project')
    likes = models.PositiveIntegerField(default=0)
    my_role = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('maintained', 'Maintained'),
        ('archived', 'Archived')
    ], default='completed')
    team_size = models.PositiveIntegerField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-featured', '-created_date']


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current position")
    location = models.CharField(max_length=100, blank=True)
    company_url = models.URLField(blank=True, validators=[URLValidator()])
    
    @property
    def is_current(self):
        return self.end_date is None
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    gpa = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
    class Meta:
        ordering = ['-start_date']


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_date']


class ProjectComment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Comment by {self.name} on {self.project.title}"
    
    class Meta:
        ordering = ['-created_at']


class ProjectBookmark(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_bookmarks')
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Bookmark for {self.project.title}"
    
    class Meta:
        unique_together = ('project', 'session_key')


class ProjectLike(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_likes')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Like for {self.project.title}"
    
    class Meta:
        unique_together = ('project', 'ip_address')


class ProjectRating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    ip_address = models.GenericIPAddressField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Rating {self.rating} for {self.project.title}"
    
    class Meta:
        unique_together = ('project', 'ip_address')


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='documents/', blank=True, null=True)
    
    # Social Links
    github_url = models.URLField(blank=True, validators=[URLValidator()])
    linkedin_url = models.URLField(blank=True, validators=[URLValidator()])
    twitter_url = models.URLField(blank=True, validators=[URLValidator()])
    website_url = models.URLField(blank=True, validators=[URLValidator()])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
