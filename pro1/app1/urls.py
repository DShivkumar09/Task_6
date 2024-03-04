from django.urls import path
from .views import UploadExcel, ProductList

urlpatterns = [
    path('upload/', UploadExcel.as_view(), name='upload'),
    path('products/', ProductList.as_view(), name='list'),
]
