from django.urls import path
from .views import MyModelListView

urlpatterns = [
    path('', MyModelListView.as_view(), name='mymodel_list'),
]

