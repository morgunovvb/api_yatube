from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
