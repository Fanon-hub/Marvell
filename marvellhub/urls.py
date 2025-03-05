from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include router-generated API URLs
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Serves the index.html page
]
