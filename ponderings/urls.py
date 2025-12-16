from django.urls import path, re_path

from . import views

app_name = "ponderings"
urlpatterns = [
    # ex: /ponderings
    re_path(r'^/?$', views.PonderingIndexView.as_view(), name="pondering-index"),
    # ex: /ponderings/add
    path("/add", views.PonderingCreateView.as_view(), name="pondering-add"),
    # ex: /ponderings/5
    path("/<int:pk>", views.PonderingDetailView.as_view(), name="pondering-detail"),
    # ex: /ponderings/5/edit
    path("/<int:pk>/edit", views.PonderingUpdateView.as_view(), name="pondering-edit"),
    # ex: /ponderings/5/delete
    path("/<int:pk>/delete", views.PonderingDeleteView.as_view(), name="pondering-delete"),
]