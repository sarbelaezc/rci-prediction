from django.urls import include, path
from rest_framework import routers

from prediction import views

urlpatterns = [
    # ---------- Trains the defined model ----------
    path(
        'train_model/',
        views.TrainModelView.as_view(),
        name='train-model'
    ),
    # ------- Predict over the trained model -------
    path(
        'predict/',
        views.PredictView.as_view(),
        name='predict'
    )
    
]
