from django import template
from django.core.urlresolvers import reverse
from datetime import date, timedelta
from django.db.models import Sum
from five_years.models import Income, LivingExpense, InterpersonalCircle, ExtendKnowledge, Holiday, Saving, Fund
from django.contrib.humanize.templatetags.humanize import intcomma
import re
from django.conf import settings

register = template.Library()


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


@register.filter(name='titleize')
def titleize(name):
    result = first_cap_re.sub(r'\1 \2', name)
    return all_cap_re.sub(r'\1 \2', result).lower()


@register.filter(name='pdb')
def pdb(element):
    import pdb
    pdb.set_trace()

    return element


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='transaction_flow')
def transaction_flow(transaction_field):
    if transaction_field == 0:
        return 'in'
    else:
        return 'out'


@register.simple_tag
def active(request, app_name, named_url, prefix=''):
    if request.path == reverse(app_name + ':' + named_url):
        return prefix + 'active'
    return ''


@register.simple_tag
def active_class_for_listing(request, prefix):
    app_name = 'five_years'
    named_urls = ['list-living-expense', 'list-interpersonal-circle', 'list-extend-knowledge', 'list-holiday', 'list-saving']

    for named_url in named_urls:
        if request.path in reverse(app_name + ':' + named_url):
            return prefix + 'active'
    return ''


@register.simple_tag
def active_class_for_adding(request, prefix):
    app_name = 'five_years'
    named_urls = ['add-living-expense', 'add-interpersonal-circle', 'add-extend-knowledge', 'add-holiday', 'add-saving']

    for named_url in named_urls:
        if request.path in reverse(app_name + ':' + named_url):
            return prefix + 'active'
    return ''


@register.simple_tag
def fund_transaction(request, FundModel, transaction_flow='in', delta_days=0):
    transaction_flow = (0 if transaction_flow == 'in' else (1 if transaction_flow == 'out' else 3))
    FundModel = Fund(FundModel)
    if delta_days > 0:
        today = date.today() + timedelta(days=1)
        delta = timedelta(days=delta_days)
        past = today - delta
        if transaction_flow < 2:  # transaction in
            result = FundModel.objects.filter(done_at__lte=today, done_at__gt=past, transaction=transaction_flow).aggregate(total=Sum('value'))['total']
            result = result if result else 0
            return intcomma(result)
        else:  # balance inquiry
            total_in = FundModel.objects.filter(done_at__range=(past, today), transaction=0).aggregate(total=Sum('value'))['total']
            total_out = FundModel.objects.filter(done_at__range=(past, today), transaction=1).aggregate(total=Sum('value'))['total']
            total_in = total_in if total_in else 0
            total_out = total_out if total_out else 0
            return intcomma(total_in - total_out)

    else:
        if transaction_flow < 2:  # transaction in
            result = FundModel.objects.filter(transaction=transaction_flow).aggregate(total=Sum('value'))['total']
            result = result if result else 0
            return intcomma(result)
        else:  # balance inquiry
            total_in = FundModel.objects.filter(transaction=0).aggregate(total=Sum('value'))['total']
            total_out = FundModel.objects.filter(transaction=1).aggregate(total=Sum('value'))['total']
            total_in = total_in if total_in else 0
            total_out = total_out if total_out else 0
            return intcomma(total_in - total_out)


@register.simple_tag
def print_fund_summary(request, FundModel):
    html = '<ul><li><strong>This Week</strong><br>'
    html += '<i class="glyphicon glyphicon-save"></i> IDR ' + fund_transaction(request, FundModel, 'in', 7) + '<br>'
    html += '<i class="glyphicon glyphicon-open"></i> IDR ' + fund_transaction(request, FundModel, 'out', 7) + '<br>'
    html += '<i class="glyphicon glyphicon-usd"></i> IDR ' + fund_transaction(request, FundModel, 'balance', 7) + '<br><br></li>'

    html += '<li><strong>This Month</strong><br>'
    html += '<i class="glyphicon glyphicon-save"></i> IDR ' + fund_transaction(request, FundModel, 'in', 30) + '<br>'
    html += '<i class="glyphicon glyphicon-open"></i> IDR ' + fund_transaction(request, FundModel, 'out', 30) + '<br>'
    html += '<i class="glyphicon glyphicon-usd"></i> IDR ' + fund_transaction(request, FundModel, 'balance', 30) + '<br><br></li>'

    html += '<li><strong>All The Time</strong><br>'
    html += '<i class="glyphicon glyphicon-save"></i> IDR ' + fund_transaction(request, FundModel, 'in') + '<br>'
    html += '<i class="glyphicon glyphicon-open"></i> IDR ' + fund_transaction(request, FundModel, 'out') + '<br>'
    html += '<i class="glyphicon glyphicon-usd"></i> IDR ' + fund_transaction(request, FundModel, 'balance') + '<br><br></li></ul>'

    return html


@register.filter(name='is_login_url')
def is_login_url(request):
    login_url = reverse('five_years:login')
    if request.path == login_url or request.path == settings.LOGOUT_REDIRECT_URL:
        return True
    return False
