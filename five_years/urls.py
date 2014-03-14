from django.conf.urls import patterns, url
from five_years import views, auth_views
from income_management import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^logout[/]?$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^dashboard[/]?$', views.DashboardView.as_view(), name='dashboard'),

    url(r'^add-living-expense[/]?$', views.LivingExpenseCreate.as_view(), name='add-living-expense'),
    url(r'^add-interpersonal-circle[/]?$', views.InterpersonalCircleCreate.as_view(), name='add-interpersonal-circle'),
    url(r'^add-extend-knowledge[/]?$', views.ExtendKnowledgeCreate.as_view(), name='add-extend-knowledge'),
    url(r'^add-holiday[/]?$', views.HolidayCreate.as_view(), name='add-holiday'),
    url(r'^add-saving[/]?$', views.SavingCreate.as_view(), name='add-saving'),

    url(r'^list-living-expense[/]?$', views.LivingExpenseList.as_view(), name='list-living-expense'),
    url(r'^list-interpersonal-circle[/]?$', views.InterpersonalCircleList.as_view(), name='list-interpersonal-circle'),
    url(r'^list-extend-knowledge[/]?$', views.ExtendKnowledgeList.as_view(), name='list-extend-knowledge'),
    url(r'^list-holiday[/]?$', views.HolidayList.as_view(), name='list-holiday'),
    url(r'^list-saving[/]?$', views.SavingList.as_view(), name='list-saving'),

    url(r'^add-income[/]?$', views.IncomeCreate.as_view(), name='add-income'),
    url(r'^list-income[/]?$', views.IncomeList.as_view(), name='list-income'),
    url(r'^login[/]?$', auth_views.LoginView.as_view(success_url='dashboard'), name='login'),
    url(r'^$', auth_views.LoginView.as_view(success_url='dashboard'), name='login'),
)

from django.template.loader import add_to_builtins
for tag in settings.AUTOLOAD_TEMPLATETAGS:
    add_to_builtins(tag)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

urlpatterns += staticfiles_urlpatterns()
