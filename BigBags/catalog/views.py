from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bag, colours, BookInstance, material, Modification
from .forms import ChooseColor, ChooseMaterial, ChooseStatus
from django.views import generic, View
from django.views.generic.edit import CreateView
from .forms import BagForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import UserForm
def index (request):
    return render (request, 'index.html')

def check (request):
    model=Modification.objects.all()
    return render (request, 'registration/check.html', {'mod':model})

def madeorder (request):
    return render (request, 'catalog/make_order.html')

class BagsListView (generic.FormView, generic.ListView):
    model = Bag
    template_name = 'catalog/bag_list.html'
    form_class = BagForm
    paginate_by = 9

class BagDetailView(generic.DetailView):
    model = Bag
    form=UserForm()
    extra_context = {'latest': Modification.objects.all(),'form':form}


class LoanedBagByUserListView (LoginRequiredMixin, generic.ListView):

    model = Bag
    template_name = 'catalog/bookinstance_list_backet_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Bag.objects.filter(Basket=self.request.user).filter(status__exact='2')

class RegisterUser (CreateView):
    form_class = UserCreationForm
    template_name = 'catalog/register.html'
    success_url = 'catalog/bag_list.html'

    def form_valid(self, form):
        form.save
        return super(RegisterUser, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterUser, self).form_invalid(form)
