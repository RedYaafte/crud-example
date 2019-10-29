from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import note_list, note_detail

urlpatterns = [
    path('note/', note_list),
    path('note/<int:pk>/', note_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)