"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from manager.views import signin_view, signup_view, logout_view, show_applications_view
from manager.views import create_new_application
from manager.views import show_start_page

from manager.views import show_today_applications
from manager.views import show_info_application
from manager.views import clear_application_view
from manager.views import show_application_for_driver
from manager.views import success_application
from manager.views import conflict_resolution_view
from manager.views import conflict_correction_view
from manager.views import approv_all_applications
from manager.views import submitted_all_applications

from manager.views import show_construction_sites_view
from manager.views import edit_construction_sites_view
from manager.views import delete_construction_sites_view
from manager.views import change_status_construction_site
from manager.views import add_construction_sites_view

from manager.views import show_staff_view
from manager.views import edit_staff_view
from manager.views import del_staff

from manager.views import tabel_driver_view
from manager.views import tabel_workday_view
from manager.views import Technic_Driver_view

from manager.views import driver_app_list_view
from manager.views import foreman_app_list_view

from manager.views import append_in_hos_tech
from manager.views import redirect_view


urlpatterns = [
    # re_path(r'.*', redirect_view),
    path('', show_start_page, name='start_page'),
    path('applications/<str:day>', show_applications_view, name='application_list'),
    path('applications/<int:id_user>/<str:day>', show_applications_view, name='application_list'),
    path('append_in_hos_tech/<int:id_drv>', append_in_hos_tech, name='append_in_hos_tech'),

    path('construction_sites/', show_construction_sites_view, name='construction_sites'),
    path('edit_construction_sites/<int:id_construction_sites>', edit_construction_sites_view, name='edit_construction_sites'),
    path('delete_construction_sites/<int:id_construction_sites>', delete_construction_sites_view, name='delete_construction_sites'),
    path('change_status_construction_site/<int:id_construction_sites>', change_status_construction_site, name='change_status_construction_site'),
    path('add_construction_sites/', add_construction_sites_view, name='add_construction_sites'),

    path('show_staff/', show_staff_view, name='show_staff'),
    path('edit_staff/<int:id_staff>', edit_staff_view, name='edit_staff'),
    path('del_staff/<int:id_staff>', del_staff, name='del_staff'),


    path('tabel_driver/<str:day>', tabel_driver_view, name='tabel_driver'),
    path('tabel_workday/<str:ch_week>', tabel_workday_view, name='tabel_workday'),
    path('technic_driver/<str:day>', Technic_Driver_view, name='technic_driver'),
    path('tech_list/<str:day>', Technic_Driver_view, name='tech_list'),

    path('admin/', admin.site.urls),
    path('signin/', signin_view, name="sign_in"),
    path('signup/', signup_view, name="sign_up"),
    path('logout', logout_view, name="logout"),

    path('today_app/<str:day>', show_today_applications, name="show_today_applications"),
    path('info_app/<int:id_application>', show_info_application, name="show_info_application"),
    path('new_app/<int:id_application>', create_new_application, name="add_application"),
    path('clear_app/<int:id_application>', clear_application_view, name='clear_application'),
    path('success_app/<int:id_application>', success_application, name='success_application'),
    path('conflict_resolution/<str:day>', conflict_resolution_view, name="conflict_resolution"),
    path('conflict_correction/<str:day>/<str:id_applications>', conflict_correction_view, name="conflict_correction"),

    path('personal_application/<str:day>/<str:id_user>', show_application_for_driver, name='application_for_driver'),

    path('driver_app_list/<str:day>', driver_app_list_view, name='driver_app_list'),
    path('foreman_app_list/<str:day>', foreman_app_list_view, name='foreman_app_list'),



    path('approv_all_applications/<str:day>', approv_all_applications, name='approv_all_applications'),
    path('submitted_all_applications/<str:day>', submitted_all_applications, name='submitted_all_applications'),
    re_path(r'.*', redirect_view),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
