from django.urls import  path
from agents.views import (
    AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView,
    AgentDeleteView
    )

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name="agents-list" ),
    path('<int:pk>/', AgentDetailView.as_view(), name="agent-details"),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name="agent-update"),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name="agent-delete"),
    path('create/', AgentCreateView.as_view(), name="agents-create" ),
]