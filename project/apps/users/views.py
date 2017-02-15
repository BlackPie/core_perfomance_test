from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View

from project.apps.users.models import User
from project.apps.users.export import generate_xls


class UserListView(ListView):
    model = User
    template_name = 'apps/users/list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'apps/users/detail.html'


class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'number', 'birthday']
    template_name = 'apps/users/update.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'birthday']
    template_name = 'apps/users/create.html'
    success_url = reverse_lazy('user_list')


class UserExportView(View):
    def get(self, *args, **kwargs):
        response = HttpResponse(content_type="application/ms-excel")
        response['Content-Disposition'] = 'attachment; filename=export.xls'
        workbook = generate_xls()
        workbook.save(response)
        return response
