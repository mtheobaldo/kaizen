from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView 
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Idea, Profile, Category, Comment
from django.core.urlresolvers import reverse, reverse_lazy

# Create your views here.
class IdeaListView(ListView):
    model = Idea


class IdeaCategoryView(ListView):
	def get_queryset(self, *args, **kwargs):
		return Idea.objects.filter(category__id=self.kwargs.get('pk'))

class IdeaDetailView(DetailView):
	model = Idea

class SecretView(TemplateView):
    template_name="kaizen/secret.html"

class ChangeStatusView(UpdateView):
	model = Idea
	fields = ['status']
	def get_success_url(self):
		return reverse('kaizen:ideadetail', args=(self.object.pk,))

class EditIdeaView(UpdateView):
	model = Idea
	fields = ['title', 'description', 'category']
	def get_success_url(self):
		return reverse('kaizen:ideadetail', args=(self.object.pk,))

class NewIdeaView(CreateView):
	model = Idea
	fields = ("title", "description", "category")

	def get_success_url(self):
		return reverse('kaizen:ideadetail', args=(self.object.pk,))

	def form_valid(self, form):
		idea = form.save(commit=False)
		idea.profile = Profile.objects.get(user=self.request.user)
		idea.save()
		return super(NewIdeaView, self).form_valid(form)

class IdeaDeleteView(DeleteView):
	model = Idea

	def get_success_url(self):
		return reverse('kaizen:success')

class NewCommentView(CreateView):
	model = Comment
	fields = ("comment_text",)
	success_url = reverse_lazy('kaizen:success')


	def form_valid(self, form):
		comment = form.save(commit=False)
		comment.idea = Idea.objects.get(pk=self.kwargs.get("pk"))
		comment.save()
		return super(NewCommentView, self).form_valid(form)
