from django.urls import path
from website.views import MainView, KontaktView, ReferencjeView, CertyfikatyView, RealizacjeView, AlarmyView, \
    PolitykaView, MonitoringCCTVView, ElektrykaView, DomofonyView, SieciView, ONasView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('kontakt', KontaktView.as_view(), name='kontakt'),
    path('referencje', ReferencjeView.as_view(), name='referencje'),
    path('certyfikaty', CertyfikatyView.as_view(), name='certyfikaty'),
    path('realizacje', RealizacjeView.as_view(), name='realizacje'),
    path('alarmy', AlarmyView.as_view(), name='alarmy'),
    path('polityka', PolitykaView.as_view(), name='polityka'),
    path('monitoring', MonitoringCCTVView.as_view(), name='monitoring'),
    path('elektryka', ElektrykaView.as_view(), name='elektryka'),
    path('sieci', SieciView.as_view(), name='sieci'),
    path('domofony', DomofonyView.as_view(), name='domofony'),
    path('o-nas', ONasView.as_view(), name='o-nas'),
]