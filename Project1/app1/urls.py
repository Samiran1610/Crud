# urls.py
from django.urls import path # type: ignore
from Sample_Django.Project1.Project1 import settings
from app1 import views
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
urlpatterns = [
    path("add/", views.details, name="add_patient"),
    path("patient/<str:Name>/", views.display, name="view_patient"),
    path('all/', views.view_all_patients, name='view_all_patients'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    # Add other paths as needed
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]