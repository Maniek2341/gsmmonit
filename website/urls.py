from django.urls import path
from website.views import MainView, KontaktView, ReferencjeView, CertyfikatyView, RealizacjeView, AlarmyView, \
    PolitykaView, MonitoringCCTVView, ElektrykaView, DomofonyView, SieciView, ONasView, \
    UslugiSerwisoweView, MonitoringGSMView, KontrolaDostepuView, MonitoringMobilnyView, UslugiDodatkoweView, RCPView, \
    SponsoringView, PPOZView

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
    path('videodomofony', DomofonyView.as_view(), name='videodomofony'),
    path('monitoring-mobilny', MonitoringMobilnyView.as_view(), name='monitoring-mobilny'),
    path('uslugi-dodatkowe', UslugiDodatkoweView.as_view(), name='uslugi-dodatkowe'),
    path('rcp', RCPView.as_view(), name='rcp'),
    path('sponsoring', SponsoringView.as_view(), name='sponsoring'),
    path('ppoz', PPOZView.as_view(), name='ppoz'),
]