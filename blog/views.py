from config import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from blog.models import Record
from pytils.translit import slugify


class RecordListView(ListView):
    model = Record

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class RecordCreateView(CreateView):
    model = Record
    fields = ('name', 'content', 'image', 'created_at', 'is_published')
    success_url = reverse_lazy('blog:record_list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.name)
            new_rec.save()
        return super().form_valid(form)


class RecordDetailView(DetailView):
    model = Record

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail('Поздравление', 'Твою запись посмотрели 100 раз!', settings.EMAIL_HOST_USER, ['dan14n97@gmail.com'])
        return self.object


class RecordUpdateView(UpdateView):
    model = Record
    fields = ('name', 'content', 'image', 'created_at', 'is_published')
    # success_url = reverse_lazy('blog:record_list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.name)
            new_rec.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:record_detail', args=[self.kwargs.get('pk')])


class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('blog:record_list')
