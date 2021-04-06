from django.urls import path
from employee import views
app_name="employee"

urlpatterns = [
    path('',views.emp, name='emp'),
    path('/show', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('destroy/<int:id>', views.destroy, name='distroy'),
]