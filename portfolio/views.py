from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Project, Skill, Experience, Education, Profile, Contact
from .forms import ContactForm
import json


def home(request):
    """Home page view with featured projects and skills"""
    try:
        profile = Profile.objects.first()
        featured_projects = Project.objects.filter(featured=True)[:3]
        skills = Skill.objects.all()[:8]  # Top 8 skills
        experiences = Experience.objects.order_by('-start_date')[:3]  # Recent 3 experiences
        
        context = {
            'profile': profile,
            'featured_projects': featured_projects,
            'skills': skills,
            'experiences': experiences,
        }
        return render(request, 'portfolio/home.html', context)
    except Exception as e:
        # Fallback context in case of any errors
        context = {
            'profile': None,
            'featured_projects': [],
            'skills': [],
            'experiences': [],
        }
        return render(request, 'portfolio/home.html', context)


def about(request):
    """About page with detailed profile, experience, and education"""
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)


def projects(request):
    """Projects page with all projects"""
    all_projects = Project.objects.select_related().prefetch_related('technologies')
    technologies = Skill.objects.all()
    
    # Filter by technology if specified
    tech_filter = request.GET.get('tech')
    if tech_filter:
        all_projects = all_projects.filter(technologies__name__icontains=tech_filter)
    
    context = {
        'projects': all_projects,
        'technologies': technologies,
        'current_filter': tech_filter,
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, project_id):
    """Individual project detail page"""
    project = get_object_or_404(Project.objects.prefetch_related('technologies'), id=project_id)
    related_projects = Project.objects.exclude(id=project_id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)


def contact(request):
    """Contact page with contact form"""
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # AJAX request
            return handle_ajax_contact(request, profile)
        else:
            # Regular form submission
            return handle_regular_contact(request, profile)
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'portfolio/contact.html', context)


def handle_ajax_contact(request, profile):
    """Handle AJAX contact form submission"""
    try:
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save contact message
            contact_message = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                    message=f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[profile.email if profile else 'your-email@example.com'],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! I\'ll get back to you soon.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please correct the errors below.',
                'errors': form.errors
            })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred while sending your message.'
        })


def handle_regular_contact(request, profile):
    """Handle regular contact form submission"""
    form = ContactForm(request.POST)
    if form.is_valid():
        # Save contact message
        contact_message = form.save()
        
        # Send email notification (optional)
        try:
            send_mail(
                subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                message=f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[profile.email if profile else 'your-email@example.com'],
                fail_silently=True,
            )
        except:
            pass  # Email sending is optional
        
        messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
        return redirect('contact')
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'portfolio/contact.html', context)


# API Views for AJAX functionality

def projects_api(request):
    """API endpoint for projects with filtering and pagination"""
    try:
        # Get filter parameters
        filter_param = request.GET.get('filter', 'all')
        page = int(request.GET.get('page', 1))
        per_page = 6
        
        # Filter projects
        projects = Project.objects.select_related().prefetch_related('technologies')
        
        if filter_param != 'all':
            projects = projects.filter(
                Q(technologies__name__icontains=filter_param) |
                Q(technologies__category__icontains=filter_param)
            ).distinct()
        
        # Paginate
        paginator = Paginator(projects, per_page)
        page_obj = paginator.get_page(page)
        
        # Serialize projects
        projects_data = []
        for project in page_obj:
            projects_data.append({
                'id': project.id,
                'title': project.title,
                'short_description': project.short_description,
                'image': project.image.url if project.image else None,
                'github_url': project.github_url,
                'live_url': project.live_url,
                'technologies': [tech.name for tech in project.technologies.all()],
                'featured': project.featured,
                'created_date': project.created_date.strftime('%B %Y')
            })
        
        return JsonResponse({
            'success': True,
            'projects': projects_data,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'current_page': page,
            'total_pages': paginator.num_pages
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })


def project_detail_api(request, project_id):
    """API endpoint for individual project details"""
    try:
        project = get_object_or_404(Project.objects.prefetch_related('technologies'), id=project_id)
        
        project_data = {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'short_description': project.short_description,
            'image': project.image.url if project.image else None,
            'github_url': project.github_url,
            'live_url': project.live_url,
            'technologies': [tech.name for tech in project.technologies.all()],
            'featured': project.featured,
            'created_date': project.created_date.strftime('%B %d, %Y'),
            'updated_date': project.updated_date.strftime('%B %d, %Y')
        }
        
        return JsonResponse(project_data)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })


def skills_api(request):
    """API endpoint for skills data (for charts/animations)"""
    try:
        skills = Skill.objects.all()
        skills_data = []
        
        for skill in skills:
            skills_data.append({
                'name': skill.name,
                'proficiency': skill.proficiency,
                'category': skill.category,
                'icon': skill.icon,
            })
        
        return JsonResponse({
            'success': True,
            'skills': skills_data
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })


def resume_download(request):
    """Handle resume download"""
    profile = Profile.objects.first()
    if profile and profile.resume:
        # Redirect to the resume file
        return redirect(profile.resume.url)
    else:
        messages.error(request, 'Resume not available.')
        return redirect('about')


# Additional utility views

def search_projects(request):
    """Search projects by title, description, or technology"""
    query = request.GET.get('q', '')
    if not query:
        return JsonResponse({'projects': []})
    
    try:
        projects = Project.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(short_description__icontains=query) |
            Q(technologies__name__icontains=query)
        ).distinct()[:10]
        
        results = []
        for project in projects:
            results.append({
                'id': project.id,
                'title': project.title,
                'short_description': project.short_description,
                'url': f'/project/{project.id}/',
                'image': project.image.url if project.image else None
            })
        
        return JsonResponse({'projects': results})
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })


def contact_stats(request):
    """Get contact statistics for admin"""
    if not request.user.is_staff:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    try:
        total_messages = Contact.objects.count()
        unread_messages = Contact.objects.filter(is_read=False).count()
        recent_messages = Contact.objects.order_by('-created_date')[:5]
        
        recent_data = []
        for msg in recent_messages:
            recent_data.append({
                'name': msg.name,
                'subject': msg.subject,
                'created_date': msg.created_date.strftime('%Y-%m-%d %H:%M'),
                'is_read': msg.is_read
            })
        
        return JsonResponse({
            'total_messages': total_messages,
            'unread_messages': unread_messages,
            'recent_messages': recent_data
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })
