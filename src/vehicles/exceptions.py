from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class FieldNotAllowed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Field "{field}" not allowed.')
    default_code = 'field_not_allowed'

    def __init__(self, field, detail=None, code=None):
        if detail is None:
            detail = force_str(self.default_detail).format(field=field)
        super().__init__(detail, code)
