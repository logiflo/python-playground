"""Defines URL patterns for learning_logs.
"""

from django.urls import path
from . import views

urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    #Topic page : show all topics
    path('topics/', views.topics, name='topics'),

    #Detail page for a single topic
    path('topics/<topic_id>/', views.topic, name='topic'),

    #Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]

