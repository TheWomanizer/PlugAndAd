from django.urls import path
from .views import AdsSummaryView, AdsTimeseriesView

urlpatterns = [
    path('ads/summary/', AdsSummaryView.as_view(), name='ads_summary'),
    path('ads/timeseries/', AdsTimeseriesView.as_view(), name='ads_timeseries'),
]