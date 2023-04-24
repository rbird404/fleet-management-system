from django.db.models.signals import pre_save
from cars.models import Car, Engine, Distribution, Waybill, Passport
from history.models import History, TYPES
from django.db.models import Model

__all__ = (
    'car_changes_tracker',
    'engine_changes_tracker',
    'distribution_changes_tracker',
    'waybill_changes_tracker',
    'passport_changes_tracker'
)


def tracker_model_field_changes(sender, instance, **kwargs):
    # use only pre_save
    if instance.id is None:
        pass
    else:
        current = instance
        previous = sender.objects.get(id=instance.id)
        for field in (field.name for field in sender._meta.get_fields()):
            if field == 'created_at' and field == 'updated_at':
                continue
            current_value = getattr(current, field)
            previous_value = getattr(previous, field)
            if current_value != previous_value:
                if isinstance(current_value, Model):
                    current_value = current_value.pk

                value_type = TYPES[type(current_value)]

                History.objects.create(
                    content_object=previous,
                    field=field,
                    value=current_value,
                    value_type=value_type
                )


car_changes_tracker = pre_save.connect(
    tracker_model_field_changes, sender=Car
)
engine_changes_tracker = pre_save.connect(
    tracker_model_field_changes, sender=Engine
)
distribution_changes_tracker = pre_save.connect(
    tracker_model_field_changes, sender=Distribution
)
waybill_changes_tracker = pre_save.connect(
    tracker_model_field_changes, sender=Waybill
)
passport_changes_tracker = pre_save.connect(
    tracker_model_field_changes, sender=Passport
)
