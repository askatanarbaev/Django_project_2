from django.urls import path
from .views import (reply_topic, BoardListView, BoardDetailTopicListView, NewTopicView, 
                    PostListView, EditPostView, DeletePostView, DeleteTopic)


urlpatterns = [
    # path('home/', home, name='home'),
    # path('board/<int:pk>/', board_topics, name='board_topics'),
    # path('board/<int:pk>/new/', new_topic, name='new_topic'),
    # path('board/<int:pk>/<int:topic_pk>/', topic_posts, name='topic_posts'),
    path('home/', BoardListView.as_view(), name='home'),
    path('board/<int:pk>/',BoardDetailTopicListView.as_view(), name='board_topics'),
    path('board/<int:pk>/new/', NewTopicView.as_view(), name='new_topic'),
    path('board/<int:pk>/<int:topic_pk>/', PostListView.as_view(), name='topic_posts'),
    path('board/<int:pk>/topics/<int:topic_pk>/delete', DeleteTopic.as_view(), name='delete_topic'),
    path('board/<int:pk>/topics/<int:topic_pk>/reply/', reply_topic, name='reply_topic'),
    path('board/<int:pk>/topics/<int:topic_pk>/<int:post_pk>/edit', EditPostView.as_view(), name='edit_post'),
    path('board/<int:pk>/topics/<int:topic_pk>/<int:post_pk>/delete', DeletePostView.as_view(), name='delete_post'),
    
]