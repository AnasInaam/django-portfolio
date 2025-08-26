from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume_download, name='resume_download'),
    
    # API endpoints
    path('api/projects/', views.projects_api, name='projects_api'),
    path('api/project/<int:project_id>/', views.project_detail_api, name='project_detail_api'),
    path('api/skills/', views.skills_api, name='skills_api'),
    path('api/search/projects/', views.search_projects, name='search_projects'),
    path('api/contact/stats/', views.contact_stats, name='contact_stats'),
    # SEO files
    path('sitemap.xml', views.sitemap_xml, name='sitemap'),
    path('robots.txt', views.robots_txt, name='robots'),
]
