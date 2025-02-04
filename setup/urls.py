"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import TaskListView, TaskUpsdateView, TaskDeleteView, TaskCreateView
#from tasks.views import task_list

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',task_list)
    path('', TaskListView.as_view(), name = 'task-list'),
    path('tasks/<int:pk>/edit/', TaskUpsdateView.as_view(), name = 'task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name = 'task-delete'),
    path('tasks/create/', TaskCreateView.as_view(), name = 'task-create'),
    path('account/', include('account.urls'))


]
