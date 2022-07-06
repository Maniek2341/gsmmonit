from django.urls import path
from website.views import MainView, KontaktView, ReferencjeView, CertyfikatyView, RealizacjeView, AlarmyView, \
    PolitykaView, MonitoringCCTVView, ElektrykaView, DomofonyView, SieciView, ONasView, VideoDomofonyView, \
    UslugiSerwisoweView, MonitoringGSMView, KontrolaDostepuView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('kontakt', KontaktView.as_view(), name='kontakt'),
    path('referencje', ReferencjeView.as_view(), name='referencje'),
    path('certyfikaty', CertyfikatyView.as_view(), name='certyfikaty'),
    path('realizacje', RealizacjeView.as_view(), name='realizacje'),
    path('alarmy', AlarmyView.as_view(), name='alarmy'),
    path('polityka', PolitykaView.as_view(), name='polityka'),
    path('monitoring-cctv', MonitoringCCTVView.as_view(), name='monitoring-cctv'),
    path('elektryka', ElektrykaView.as_view(), name='elektryka'),
    path('sieci', SieciView.as_view(), name='sieci'),
    path('domofony', DomofonyView.as_view(), name='domofony'),
    path('o-nas', ONasView.as_view(), name='o-nas'),
    path('serwisy', UslugiSerwisoweView.as_view(), name='serwisy'),
    path('monitoring-gsm', MonitoringGSMView.as_view(), name='monitoring-gsm'),
    path('kontrola-dostepu', KontrolaDostepuView.as_view(), name='kontrola'),
    path('videodomofony', VideoDomofonyView.as_view(), name='videodomofony'),
]