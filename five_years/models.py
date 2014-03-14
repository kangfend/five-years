from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from decimal import Decimal
from datetime import date, timedelta


FORMULA = {
    'living expense': 0.3,
    'interpersonal cirlcle': 0.2,
    'extend knowledge': 0.15,
    'holiday': 0.1,
    'saving': 0.25,

    # abbrievated
    'le': 0.3,
    'ic': 0.2,
    'ek': 0.15,
    'h': 0.1,
    's': 0.25,
}


TRANSACTION = (
    (0, 'in'),
    (1, 'out'),
)


class Source(models.Model):
    """
    Source of income, can come from Salary, Project, Service, etc.
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Income(models.Model):
    source = models.ForeignKey(Source)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=25, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added_at']

    def __unicode__(self):
        return self.name

    def total_this_week(self):
        today = date.today()
        delta = timedelta(days=7)
        one_week_ago = today - delta

        return self.objects.filter(added_at__lt=today, added_at__gt=one_week_ago).aggregate(total=models.Sum('value'))['total']

    @property
    def total_this_month(self):
        today = date.today()
        delta = timedelta(days=30)
        one_week_ago = today - delta

        return self.objects.filter(added_at__lt=today, added_at__gt=one_week_ago).aggregate(total=models.Sum('value'))['total']

    @property
    def total_all(self):
        return self.objects.all().aggregate(total=models.Sum('value'))['total']


class FundModel(models.Model):
    income = models.ForeignKey(Income, blank=True, null=True)  # filled only if the transaction type is in
    value = models.DecimalField(max_digits=25, decimal_places=2)
    transaction = models.SmallIntegerField(choices=TRANSACTION, default=1, db_index=True, verbose_name='transaction flow')
    description = models.TextField(blank=True, null=True)
    done_at = models.DateTimeField(db_index=True)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-done_at', '-added_at']

    def __unicode__(self):
        return "%s" % (self.done_at,)


class LivingExpense(FundModel):
    pass


class InterpersonalCircle(FundModel):
    pass


class ExtendKnowledge(FundModel):
    pass


class Holiday(FundModel):
    pass


class Saving(FundModel):
    pass


def Fund(class_name):
    classes = {
        # text base
        'living expense': LivingExpense,
        'interpersonal circle': InterpersonalCircle,
        'extend knowledge': ExtendKnowledge,
        'holiday': Holiday,
        'saving': Saving,

        # class base
        'LivingExpense': LivingExpense,
        'InterpersonalCircle': InterpersonalCircle,
        'ExtendKnowledge': ExtendKnowledge,
        'Holiday': Holiday,
        'Saving': Saving,

        # abbrievated
        'le': LivingExpense,
        'ic': InterpersonalCircle,
        'ek': ExtendKnowledge,
        'h': Holiday,
        's': Saving
    }

    return classes[class_name]


@receiver(post_save, sender=Income)
def split_income(sender, instance, created,  **kwargs):
    if created:
        import datetime
        for ft, f in FORMULA.iteritems():
            ft = Fund(ft)(income=instance, value=(instance.value * Decimal(f)), transaction=0, description=instance.name, done_at=datetime.datetime.now())
            ft.save()
