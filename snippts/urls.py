from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippts import views

urlpatterns = [
    ## Method Based Views URLS
    # path('snippts/', views.snippet_list),
    # path('snippts/<int:pk>/', views.snippet_detail),

    ## Class Based Views URLS
    path('snippts/', views.SnippetList.as_view()),
    path('snippts/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
