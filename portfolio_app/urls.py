from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

#Ge05 part 2: adding student viewer
path('students/', views.StudentListView.as_view(), name= 'students'),
path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),

path('portfolios/', views.PortfolioDetailView.as_view(), name= 'portfolios'),
path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),

path('projects/', views.ProjectDetailView.as_view(), name= 'projects'),
path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),

]

