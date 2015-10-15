from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),

    url(r'^secrets/$', login_required(views.SecretView.as_view()), name="secret"),

    url(r'^kaizen/category/(?P<pk>\d+)/$', login_required(views.IdeaCategoryView.as_view()), name="category-ideas"),
    
    url(r'^kaizen/$', login_required(views.IdeaListView.as_view()), name="idealist"),    
    url(r'^kaizen/add/$', login_required(views.NewIdeaView.as_view()), name="newidea"),
    url(r'^kaizen/idea/(?P<pk>\d+)/$', login_required(views.IdeaDetailView.as_view()), name="ideadetail"),
    url(r'^status/idea/(?P<pk>\d+)/$', views.ChangeStatusView.as_view(), name="changestatus"),
    url(r'^update/idea/(?P<pk>\d+)/$', views.EditIdeaView.as_view(), name="editidea"),
    url(r'^delete/idea/(?P<pk>\d+)/$', login_required(views.IdeaDeleteView.as_view()), name="delete"),

    url(r'^comment/add/(?P<pk>\d+)/$', login_required(views.NewCommentView.as_view()), name="comment"),
    url(r'^comment/success/$', TemplateView.as_view(template_name="kaizen/success.html"), name="success"),

]
