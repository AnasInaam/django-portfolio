// Main JavaScript for Portfolio
document.addEventListener('DOMContentLoaded', function() {
    // Theme Toggle Functionality
    const themeToggle = document.getElementById('theme-toggle-nav');
    const htmlElement = document.documentElement;
    
    // Get stored theme or default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    htmlElement.setAttribute('data-bs-theme', currentTheme);
    
    // Update toggle button icon
    updateThemeToggleIcon(currentTheme);
    
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = htmlElement.getAttribute('data-bs-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            htmlElement.setAttribute('data-bs-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeToggleIcon(newTheme);
            
            // Add rotation animation
            themeToggle.style.transform = 'rotate(360deg)';
            setTimeout(() => {
                themeToggle.style.transform = '';
            }, 300);
        });
    }
    
    function updateThemeToggleIcon(theme) {
        const icon = document.getElementById('theme-icon');
        if (icon) {
            if (theme === 'dark') {
                icon.className = 'fas fa-sun';
            } else {
                icon.className = 'fas fa-moon';
            }
        }
    }
    
    // Loading Overlay fade out
    const loadingScreen = document.getElementById('loading-screen');
    if (loadingScreen) {
        window.addEventListener('load', () => {
            loadingScreen.classList.add('fade-out');
            setTimeout(() => loadingScreen.remove(), 600);
        });
    }
    
    // Simple Animation Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                
                // Animate skill progress bars
                const progressBars = entry.target.querySelectorAll('.progress-bar');
                progressBars.forEach(bar => {
                    const width = bar.style.width;
                    bar.style.width = '0%';
                    setTimeout(() => {
                        bar.style.width = width;
                        
                        // Animate the percentage counter
                        const skillItem = bar.closest('.skill-item');
                        if (skillItem) {
                            const percentageElement = skillItem.querySelector('.text-muted');
                            if (percentageElement && width) {
                                const targetValue = parseInt(width);
                                animateCounter(percentageElement, targetValue);
                            }
                        }
                    }, 200);
                });
            }
        });
    }, observerOptions);
    
    // Observe sections for animation
    document.querySelectorAll('.fade-in-section, section').forEach(section => {
        observer.observe(section);
    });
    
    // Smooth Scrolling for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Contact Form Enhancement
    const contactForm = document.querySelector('.contact-form-element');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
            submitBtn.disabled = true;
            
            // Get form data
            const formData = new FormData(this);
            
            // Send AJAX request
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showToast('Message sent successfully!', 'success');
                    this.reset();
                } else {
                    showToast('Failed to send message. Please try again.', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // For regular form submission fallback
                this.submit();
            })
            .finally(() => {
                // Restore button state
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
    
    // Animate number counter for skill percentages
    function animateCounter(element, targetValue) {
        const originalText = element.textContent;
        let currentValue = 0;
        const increment = targetValue / 50; // 50 steps for smooth animation
        const duration = 2000; // 2 seconds
        const stepTime = duration / 50;
        
        const counter = setInterval(() => {
            currentValue += increment;
            if (currentValue >= targetValue) {
                currentValue = targetValue;
                clearInterval(counter);
            }
            element.textContent = Math.round(currentValue) + '%';
        }, stepTime);
    }
    
    // Toast notification function
    function showToast(message, type = 'info') {
        const toastContainer = document.querySelector('.toast-container') || createToastContainer();
        
        const toastId = 'toast-' + Date.now();
        const toastHTML = `
            <div id="${toastId}" class="toast align-items-center text-bg-${type === 'error' ? 'danger' : type === 'success' ? 'success' : 'primary'} border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">
                        <i class="fas fa-${type === 'error' ? 'exclamation-circle' : type === 'success' ? 'check-circle' : 'info-circle'} me-2"></i>
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;
        
        toastContainer.insertAdjacentHTML('beforeend', toastHTML);
        
        const toast = new bootstrap.Toast(document.getElementById(toastId));
        toast.show();
        
        // Remove toast element after it's hidden
        document.getElementById(toastId).addEventListener('hidden.bs.toast', function() {
            this.remove();
        });
    }
    
    function createToastContainer() {
        const container = document.createElement('div');
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '9999';
        document.body.appendChild(container);
        return container;
    }
    
    // Back to top button
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.className = 'btn btn-primary btn-floating back-to-top';
    backToTopBtn.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: none;
        z-index: 1000;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    document.body.appendChild(backToTopBtn);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
        
        // Update navbar on scroll
        const navbar = document.querySelector('.navbar');
        if (navbar) {
            if (window.pageYOffset > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }
    });
    
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Simple hover effects for cards
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // (Removed dynamic technologies section per request)

    /* =============================
       Load More Featured Projects
       ============================= */
    const loadMoreBtn = document.getElementById('load-more-projects');
    const projectsGrid = document.getElementById('featured-projects-grid');
    if (loadMoreBtn && projectsGrid) {
        let loading = false;
        loadMoreBtn.addEventListener('click', function() {
            if (loading) return;
            loading = true;
            this.querySelector('.default-text').classList.add('d-none');
            this.querySelector('.loading-text').classList.remove('d-none');
            const nextPage = parseInt(projectsGrid.dataset.currentPage,10) + 1;
            fetch(`/api/projects/?page=${nextPage}`)
                .then(r => r.json())
                .then(data => {
                    if (data.success) {
                        projectsGrid.dataset.currentPage = nextPage;
                        const frag = document.createDocumentFragment();
                        data.projects.slice(0,3).forEach(p => {
                            const col = document.createElement('div');
                            col.className = 'col-lg-4 col-md-6 mb-4 project-item';
                            col.innerHTML = `
                                <div class="project-card card h-100 border-0 shadow-sm">
                                  <div class="project-image-wrapper position-relative overflow-hidden">
                                    ${p.image ? `<img src="${p.image}" class="card-img-top project-image" alt="${p.title}">` : `<div class='card-img-top bg-primary d-flex align-items-center justify-content-center text-white project-placeholder' style='height:200px'><i class='fas fa-laptop-code fa-2x'></i></div>`}
                                    <div class="project-overlay position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center">
                                      <div class="overlay-actions">
                                        <a href="/project/${p.id}/" class="btn btn-light btn-sm me-2"><i class="fas fa-eye"></i></a>
                                        ${p.live_url ? `<a href='${p.live_url}' target='_blank' class='btn btn-primary btn-sm'><i class='fas fa-external-link-alt'></i></a>` : ''}
                                      </div>
                                    </div>
                                  </div>
                                  <div class="card-body d-flex flex-column">
                                    <h5 class="card-title">${p.title}</h5>
                                    <p class="card-text flex-grow-1">${p.short_description}</p>
                                    <div class="technologies mb-3">${p.technologies.slice(0,3).map(t=>`<span class='badge bg-primary me-1 mb-1'>${t}</span>`).join('')}${p.technologies.length>3?`<span class='badge bg-secondary'>+${p.technologies.length-3} more</span>`:''}</div>
                                    <div class="card-actions d-flex gap-2">
                                      <a href="/project/${p.id}/" class="btn btn-outline-primary btn-sm flex-grow-1"><i class="fas fa-eye me-1"></i>View Details</a>
                                      ${p.live_url ? `<a href='${p.live_url}' class='btn btn-success btn-sm' target='_blank'><i class='fas fa-external-link-alt'></i></a>`:''}
                                    </div>
                                    <small class="text-muted mt-2"><i class='fas fa-calendar me-1'></i>${p.created_date}</small>
                                  </div>
                                </div>`;
                            frag.appendChild(col);
                        });
                        projectsGrid.appendChild(frag);
                        // Update hint
                        const hint = document.getElementById('load-more-hint');
                        if (hint) {
                            const totalShown = projectsGrid.querySelectorAll('.project-item').length;
                            hint.textContent = `Showing ${totalShown} project(s)`;
                        }
                        if (!data.has_next) {
                            loadMoreBtn.disabled = true;
                            loadMoreBtn.innerHTML = '<i class="fas fa-check me-2"></i>All Loaded';
                        }
                    } else {
                        loadMoreBtn.classList.add('btn-danger');
                        loadMoreBtn.innerHTML = '<i class="fas fa-times me-2"></i>Error';
                    }
                })
                .catch(()=>{
                    loadMoreBtn.classList.add('btn-danger');
                    loadMoreBtn.innerHTML = '<i class="fas fa-times me-2"></i>Failed';
                })
                .finally(()=>{
                    loading = false;
                    if (!loadMoreBtn.disabled) {
                        loadMoreBtn.querySelector('.default-text')?.classList.remove('d-none');
                        loadMoreBtn.querySelector('.loading-text')?.classList.add('d-none');
                    }
                });
        });
    }
});
