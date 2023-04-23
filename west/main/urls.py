import routers as routers
from django.urls import path, include
from . import views
from .views import LoginUser, ContactFormView, RegisterUser, MainViewSet


router = routers.SimpleRouter()
router.register(r'main', MainViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('contact', ContactFormView.as_view(), name='contact'),
    path('api/v1/', include(router.urls)),
#    path('api/v1/mainlist/', MainViewSet.as_view({'get': 'list'})),
#    path('api/v1/mainlist/<int:pk>/', MainViewSet.as_view({'put': 'update'})),

]
