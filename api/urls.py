from django.urls import path,include
import api.views as view

urlpatterns = [
    path('train/', view.get_train_info),
]
