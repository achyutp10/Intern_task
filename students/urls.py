from django.urls import path, include
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),  
    path('add/', StudentCreateView.as_view(), name='add_student'), 
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('api/', include(router.urls)),
]
