from django.urls import path
from . import views
from .views import (
    ProjectionListView,
    ProjectionDetailView,
    ProjectionCreateView,
    ProjectionUpdateView,
    ProjectionDeleteView,
    TicketListView,
    TicketCreateView
)

urlpatterns = [
    path('', ProjectionListView.as_view(), name='cinema-home'),
    path('post/<int:pk>/', ProjectionDetailView.as_view(), name='projection-detail'),
    path('post/new/', ProjectionCreateView.as_view(), name='projection-create'),
    #path('post/<int:pk>/update/', ProjectionUpdateView.as_view(), name='projection-update'),
    path('post/<int:pk>/delete/', ProjectionDeleteView.as_view(), name='projection-delete'),
    #path('about/', views.about, name='blog-about'),
    #path('', views.home, name='cinema-home'),
    #path('tickets/', views.tickets, name='tickets-about'),
    path('addmovie/', views.addmovie, name='addmovie'),
    path('buyticket/', views.buyTicket, name='buyticket'),
    path('tickets/', TicketListView.as_view(), name='tickets'),
    path('misc/', views.showTickets, name='misc'),
    #path('buyticket/', TicketCreateView.as_view(), name='buyticket'),
    path('obrana_zadnje_vjezbe/', views.obrana_zadnje_vjezbe, name='obrana_zadnje_vjezbe'),
    
]