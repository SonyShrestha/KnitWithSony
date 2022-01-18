from django.urls import path
from . import views

urlpatterns=[
    path("<int:item>",views.item_index_by_number),
    path("<str:item>",views.item_index)
]