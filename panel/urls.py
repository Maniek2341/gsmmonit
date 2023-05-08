from django.urls import path
from panel.views import LoginView, ForgotView, DashboardView, LogoutView, AddKlientView, KlientListView, AddRaportView, DeleteKlientView, EditKlientView, \
    RaportListView, RaportDetailView, DeleteRaportView, EditRaportView, RaportFakturaView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('forgot', ForgotView.as_view(), name='forgot'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('klient/add', AddKlientView.as_view(), name='add_klient'),
    path('klient/list', KlientListView.as_view(), name='list_klient'),
    path('raport/list', RaportListView.as_view(), name='list_raport'),
    path('raport/add', AddRaportView.as_view(), name='add_raport'),
    path('raport/remove/<int:pk>', DeleteRaportView.as_view(), name='delete_raport'),
    path('klient/remove/<int:pk>', DeleteKlientView.as_view(), name="delete_klient"),
    path('klient/edit/<int:pk>', EditKlientView.as_view(), name="edit_klient"),
    path('raport/edit/<int:pk>', EditRaportView.as_view(), name="edit_raport"),
    path('raport/detail/<int:pk>', RaportDetailView.as_view(), name="detail_raport"),
    path('raport/faktura/<int:pk>', RaportFakturaView.as_view(), name="faktura_raport"),
]