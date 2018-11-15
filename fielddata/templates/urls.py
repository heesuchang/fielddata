from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_dataset/$', views.create_dataset, name='create_dataset'),
    url(r'^edit_dataset/(?P<id>\d+)/$', views.edit_dataset, {}, name='edit_dataset'),
    url(r'^dataset_list/$', views.DatasetListView.as_view(), name='dataset_list'),
]