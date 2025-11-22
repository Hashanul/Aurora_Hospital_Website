
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from home.urls import router as supporter_router
from doctors.urls import router as supporter_router_doctor
from patients.urls import router as supporter_router_patients
from news.urls import router as supporter_router_news
from appointment.urls import router as supporter_router_appointment
from package.urls import router as supporter_router_package
from accounts.urls import router as supporter_router_accounts
from award.urls import router as supporter_router_award


# Create a single central router for all API endpoints
router = DefaultRouter()
router.registry.extend(supporter_router.registry)
router.registry.extend(supporter_router_doctor.registry)
router.registry.extend(supporter_router_patients.registry)
router.registry.extend(supporter_router_news.registry)
router.registry.extend(supporter_router_appointment.registry)
router.registry.extend(supporter_router_package.registry)
router.registry.extend(supporter_router_accounts.registry)
router.registry.extend(supporter_router_award.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 




# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework.routers import DefaultRouter
# from support_a_children.urls import router as supporter_router

# main_router = DefaultRouter()
# main_router.registry.extend(supporter_router.registry)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(main_router.urls)),
#     # Urls for user management APIs
#     path('api-auth/', include('rest_framework.urls')),
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.jwt')), # JWT based
#     path('auth/', include('djoser.urls.authtoken')), #AuthToken based

#     # Urls for core APIs
#     path('api/', include('authentication.urls')),
#     path('api/', include('child_information.urls')),
#     path('api/', include('settings.urls')),
#     path('api/', include('child_info_history.urls')),
#     path('api/', include('lrp.urls')),
#     path('api/', include('archive.urls')),
#     path('api/', include('support_a_children.urls')),
#     path('api/', include('local_child.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # static urls for media files