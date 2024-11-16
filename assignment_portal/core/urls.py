from django.urls import path
from .views import RegisterView, LoginView, AssignmentView, AdminAssignmentsView, UpdateAssignmentStatusView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('upload/', AssignmentView.as_view(), name='upload'),
    path('assignments/<int:admin_id>/', AdminAssignmentsView.as_view(), name='assignments'),
    path('assignments/<int:assignment_id>/update/', UpdateAssignmentStatusView.as_view(), name='update_assignment'),
]
