from django.urls import path
from home.views import NewProduct, Delete_product
from home import views


app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('new_product/', NewProduct.as_view(), name='new_product'),
    path('view_product/<pk>/', views.view_product, name='view_product'),
    path('edit_product/<pk>/', views.edit_product, name='edit_product'),
    path('edit_product/<pk>/delete', Delete_product.as_view(), name='delete_product'),
#    path('', HomeView.as_view(), name='home'),
#    path('connect/<operation>/<pk>/', views.change_friends, name='change_friends'),
]