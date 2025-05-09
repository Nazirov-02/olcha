from main import authentication
from django.urls import path
from main import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('products',views.ProductViewSet,basename='product-list')
router.register('categories',views.CategoryViewSet,basename='category-list')
router.register('sections',views.SectionViewSet,basename='section-list')
urlpatterns = [
    path('loginJWT',authentication.LoginJWTView.as_view()),
    path('logoutJWT',authentication.LogoutJWTView.as_view()),
]
urlpatterns += router.urls