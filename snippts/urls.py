from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippts import views

urlpatterns = [
    path('snippts/', views.snippet_list),
    path('snippts/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
