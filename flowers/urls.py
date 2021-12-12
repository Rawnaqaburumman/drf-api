from django.urls import path
from .views import FlowersListView,FlowersDetailView


urlpatterns=[
  path('',FlowersListView.as_view(), name='Flowers_list'),
  path('/<int:pk>',FlowersDetailView.as_view(), name='Flowers_details')
]