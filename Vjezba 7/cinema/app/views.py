#https://docs.djangoproject.com/en/dev/topics/db/aggregation/
from django.shortcuts import render, redirect
from .models import Projection, Ticket
from .forms import CreateMovieForm, TicketForm, BuyTicketForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Count, Min, Sum
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'projections': Projection.objects.all()
    }
    return render(request, 'app/home.html', context)


# def tickets(request):
#     return render(request, 'app/tickets.html', {'title': 'tickets'})

@login_required
def addmovie(request):
    if request.method == 'POST':
        a_form = CreateMovieForm(request.POST)
        if a_form.is_valid():
            a_form.save()
            messages.success(request, f'Your movie has been added!')
            return redirect('addmovie')
    else:
        a_form = CreateMovieForm()

    return render(request, 'app/addmovie.html', {'a_form': a_form})


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'app/tickets.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'tickets'
    fields = ['seatNumber', 'movieName', 'customer']

    def get_queryset(self):
        if self.request.user.is_superuser:
            tic = self.model.objects.all()
            return self.model.objects.all()
        return self.model.objects.filter(customer=self.request.user)

# class AdminTicketListView(LoginRequiredMixin, ListView):
#     model = Ticket

class ProjectionListView(ListView):
    model = Projection
    template_name = 'app/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'projections'
    orderring = ['movieName']


class ProjectionDetailView(DetailView):
    model = Projection

class ProjectionCreateView(LoginRequiredMixin, CreateView):
    model = Projection
    fields = ['movieName', 'cinemaHallCapacity']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ProjectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Projection
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ProjectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Projection
    fields = ['movieName', 'cinemaHallCapacity']

    def form_valid(self, form):
        #form.instance.movieName = self.request.projection.movieName
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.movieName == post.movieName:
            return True
        return False

@login_required
def buyTicket(request):
    if request.method == 'POST':
        t_form = TicketForm(request.POST)

        if t_form.is_valid():
            t_form.save()
            return redirect('cinema-home')
    else:
        t_form = TicketForm()

    context = {
        't_form': t_form,
    }
    return render(request, 'app/buyticket.html', context)

class TicketCreateView(LoginRequiredMixin, CreateView):
    form_class = TicketForm()
    template_name = 'app/buyticket.html'
    context_object_name = 't_form'
    success_url = '/'
    #fields = ['movieName', 'seatNumber']

    def form_valid(self, form):
        f = form.save(commit=False)
        f.customer = Projection.objects.get(customer=self.request.user)  # use your own profile here
        f.save()
        return HttpResponseRedirect(self.get_success_url())
        #return super(TicketCreateView, self).form_valid(form)

@login_required
def showTickets(request):

    total = 0
    temp = 0
    
    users = User.objects.all()
    for user in users:
        tickets = Ticket.objects.filter(customer=user)
        for ticket in tickets:
            temp = temp + ticket.seatNumber
        if temp > total:
            total = temp
            temp = 0
            _user = user

    tempdict = {
        'name': _user.username,
        'tickets': total
    }
    context = {
        'tickets': tempdict
    }


#     return render(request, 'app/misc.html', context)

# @login_required
# def showTickets(request):

#     total = 0
#     lst = []
#     movies = Projection.objects.all()

#     for movie in movies:
#         tickets = Ticket.objects.filter(movieName=movie)

#         for ticket in tickets:
#             total = total + ticket.seatNumber
    
#         tempdict = {
#             'name': movie.movieName,
#             'tickets': total
#         }
#         lst.append(tempdict)


#     context = {
#         'tickets': lst
#     }


#     return render(request, 'app/misc.html', context)


@login_required
def obrana_zadnje_vjezbe(request):

    total = 0
    lst = []
    users = User.objects.all()

    for user in users:
        tickets = Ticket.objects.filter(customer=user)
        
        for ticket in tickets:
            total = total + ticket.seatNumber

        if total > 5:
            status = 'True'
        elif  total >= 3 and total <= 5:
            status = 'False'
        else:
            continue

        tempdict = {
            'name': user.username,
            'total': total,
            'status':status
        }
        lst.append(tempdict)
        total = 0
        


    context = {
        'tickets': lst
    }


    return render(request, 'app/obrana_zadnje_vjezbe.html', context)
