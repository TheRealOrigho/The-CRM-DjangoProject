from django.urls import path
from .views import (
    lead_create, lead_list, lead_detail, lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView )

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list" ),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-details"),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name="assign-agent"),
]