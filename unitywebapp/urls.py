
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from blogs.views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostListView
from pages.views import IndexView, AboutListView,TeacherListView, PricingListView, CoursesListView, CalendarView
from django.contrib.auth import views as auth_views
from sendemail.views import  contactView, successView
from django.contrib import admin
from django.urls import path, include
from pdfform.views import list_pdf, upload_pdf, delete_pdf
from newsletters.views import newsletter_signup, newsletter_unsubscribe
from gallery.views import GalleryListView, GalleryCreateView, GalleryDeleteView
#from newsletters.custom_context_processor import newsletter_signup
#, newsletter_unsubscribe


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name='unity-index'),
    path('about/',AboutListView.as_view(), name='unity-about'),
    path('teacher/',TeacherListView.as_view(), name='unity-teacher'),
    path('courses/',CoursesListView.as_view(), name='unity-courses'),
    path('pricing/',PricingListView.as_view(), name='unity-pricing'),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('pdf/', list_pdf, name='list_pdf' ),
    path('pdf/upload/', upload_pdf, name='upload_pdf' ), 
    path('pdf/<int:pk>/', delete_pdf, name='delete_pdf' ),
    path('contact/',contactView, name='contact'),
    path('contact_success/', successView, name='contact_success'),
    path('calendar/',CalendarView, name='calendar'),
    path('',include('sendemail.urls')),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('gallery/add/', GalleryCreateView.as_view(), name='gallery-add'),
    path('gallery/<int:pk>delete/', GalleryDeleteView.as_view(), name='gallery-delete'),

    path('subscribe/',newsletter_signup, name='subscribe'),
    path('unsubscribe/',newsletter_unsubscribe, name='unsubscribe'),

    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)