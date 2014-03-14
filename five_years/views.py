from django.core.urlresolvers import reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from five_years.models import Income, LivingExpense, InterpersonalCircle, ExtendKnowledge, Holiday, Saving
from django.db.models import Sum
from datetime import date, timedelta
from django.template.defaultfilters import slugify
from globaltags.app_tags import titleize
from django import http


class LoggedInMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return http.HttpResponseRedirect(reverse('five_years:login'))
        return super(LoggedInMixin, self).dispatch(request, *args, **kwargs)


class DashboardView(LoggedInMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['something_else'] = None
        context['income_this_week'] = income_total_this_week()
        context['income_this_month'] = income_total_this_month()
        context['income_total'] = income_total()

        return context


def fund_balance(FundModel):
    masuk = FundModel.objects.filter(transaction=0).aggregate(total=Sum('value'))['total']
    keluar = FundModel.objects.filter(transaction=1).aggregate(total=Sum('value'))['total']

    if not masuk:
        masuk = 0
    if not keluar:
        keluar = 0

    return (masuk - keluar)


def income_total_this_week():
    today = date.today()
    one_week = timedelta(days=7)
    past = today - one_week

    return Income.objects.filter(added_at__lt=today, added_at__gt=past).aggregate(total=Sum('value'))['total']


def income_total_this_month():
    today = date.today()
    one_week = timedelta(days=30)
    past = today - one_week

    return Income.objects.filter(added_at__lt=today, added_at__gt=past).aggregate(total=Sum('value'))['total']


def income_total():
    return Income.objects.all().aggregate(total=Sum('value'))['total']


class IncomeCreate(LoggedInMixin, CreateView):
    model = Income
    template_name = 'add-income.html'
    fields = ['source', 'name', 'description', 'value']

    def get_success_url(self):
        return reverse('five_years:list-income')


class FundCreateMixin(object):
    template_name = 'add-transaction.html'
    fields = ['transaction', 'value', 'description', 'done_at']

    def dispatch(self, request, *args, **kwargs):
        return super(FundCreateMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FundCreateMixin, self).get_context_data(**kwargs)
        context['the_title'] = self.model.__name__
        return context

    def get_success_url(self):
        return reverse('five_years:list-' + slugify(titleize(self.model.__name__)))


class LivingExpenseCreate(FundCreateMixin, LoggedInMixin, CreateView):
    model = LivingExpense


class InterpersonalCircleCreate(FundCreateMixin, LoggedInMixin, CreateView):
    model = InterpersonalCircle


class ExtendKnowledgeCreate(FundCreateMixin, LoggedInMixin, CreateView):
    model = ExtendKnowledge


class HolidayCreate(FundCreateMixin, LoggedInMixin, CreateView):
    model = Holiday


class SavingCreate(LoggedInMixin, CreateView):
    model = Saving


class IncomeList(LoggedInMixin, ListView):
    model = Income
    template_name = 'list-income.html'


class FundListMixin(object):
    template_name = 'list-transaction.html'

    def dispatch(self, request, *args, **kwargs):
        return super(FundListMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(FundListMixin, self).get_context_data(**kwargs)
        context['the_title'] = self.model.__name__
        context['balance'] = fund_balance(self.model)
        return context


class LivingExpenseList(LoggedInMixin, FundListMixin, ListView):
    model = LivingExpense


class InterpersonalCircleList(LoggedInMixin, FundListMixin, ListView):
    model = InterpersonalCircle


class ExtendKnowledgeList(LoggedInMixin, FundListMixin, ListView):
    model = ExtendKnowledge


class HolidayList(LoggedInMixin, FundListMixin, ListView):
    model = Holiday


class SavingList(LoggedInMixin, FundListMixin, ListView):
    model = Saving
