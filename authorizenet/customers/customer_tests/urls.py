from django.conf.urls import url, patterns
from .views import CreateCustomerView, success_view

urlpatterns = patterns(
    '',
    url(r"^customers/create$", CreateCustomerView.as_view()),
    url(r"^success$", success_view),
)
