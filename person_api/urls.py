from django.urls import path
from .views import PersonListView, PersonDetailView, PersonFilterListView

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='person-list'),
    path('persons/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('persons/filter/', PersonFilterListView.as_view(), name='person-filter-list'),
]