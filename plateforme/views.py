from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Count

from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.utils import timezone

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms import ModelForm
#from .forms import EvenementForm
import re
from django.db.models import Q
from django.template.loader import render_to_string

from .models import Evenement, Annonce, ThemeForum, Board, Topic, Post

from django.contrib.auth.models import User
from .forms import PostForm



# Create your views here.

# TEST
def home(request):
    boards = Board.objects.all()
    return render(request, 'plateforme/home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)

    return render(request, 'plateforme/topics.html', {'board': board, 'topics': topics})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=request.user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=request.user
        )

        return redirect('plateforme:topic_posts', pk=pk, topic_pk=topic.pk)  # <- here

    return render(request, 'plateforme/new_topic.html', {'board': board})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('plateforme:topic_posts', pk=pk, topic_pk=topic_pk)
        else:
            form = PostForm() 
    return render(request, 'plateforme/topic_posts.html', {'topic': topic})

def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('plateforme:topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'plateforme/reply_topic.html', {'topic': topic, 'form': form})

class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('plateforme:post_list')
    template_name = 'plateforme/new_post.html'

#@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'plateforme/edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('plateforme:topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'plateforme/topics.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'plateforme/topic_posts.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        self.topic.views += 1
        self.topic.save()
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset






# Inscription
def inscription(request):
	return render(request, 'plateforme/inscription.html', {})

# Connexion
def connexion(request):
	return render(request, 'plateforme/connexion.html', {})

# Mot de passe oublié
def forgotpassword(request):
	return render(request, 'plateforme/forgotpassword.html', {})

# Mentions Légales
def mentionslegales(request):
	return render(request, 'plateforme/mentionslegales.html', {})

# Paiement
def paiement(request):
	return render(request, 'plateforme/paiement.html', {})

# Plan du Site
def plan(request):
	return render(request, 'plateforme/plan.html', {})

# Tableau de Bord / Changer mot de Passe
def changepassword(request):
	return render(request, 'plateforme/changepassword.html', {})

# Tableau de Bord / Infos Personnelles
def infosperso(request):
	return render(request, 'plateforme/infosperso.html', {})

# Tableau de Bord / Changer Avatar
def changeavatar(request):
	return render(request, 'plateforme/changeavatar.html', {})


# Accueil
def accueil(request):
	return render(request, 'plateforme/accueil.html', {})

# Presentation
def presentation(request):
	return render(request, 'plateforme/presentation.html', {})

# Presentation / Mission
def missions(request):
	return render(request, 'plateforme/missions.html', {})

# Presentation / Bureau
def bureau(request):
	return render(request, 'plateforme/bureau.html', {})

# Profils & Membres
def profil(request):
	return render(request, 'plateforme/profil.html', {})

# Profils & Membres / Id
def profileId(request):
	return render(request, 'plateforme/profileId.html', {})

# Profils & Membres / CV
def profileCv(request):
	return render(request, 'plateforme/profileCv.html', {})

# Actualités
def actualites(request):
	return render(request, 'plateforme/actualites.html', {})

# Test List View
class EvenementListView(ListView):

    model = Evenement

    def get_context_data(self, **kwargs):
        context = super(EvenementListView, self).get_context_data(**kwargs)
        return context

# Test DetailView
class EvenementDetailView(DetailView):

    model = Evenement

    def get_context_data(self, **kwargs):
        context = super(EvenementDetailView, self).get_context_data(**kwargs)
        success_url = reverse_lazy('plateforme:evenement_list')
        return context

# Actualités / Evènements
def evenements(request):
	return render(request, 'plateforme/evenements.html', {})



# Actualités / Evènements / Infos
def infoEvenements(request):
	infos = Evenement.objects.filter(evenement__startswith='Assemblée')
	return render(request, 'plateforme/infoEvenements.html', {'infos': infos})


# Actualités / Annonces
def annonces(request):
	annonces = Annonce.objects.all()
	return render(request, 'plateforme/annonces.html', {'annonces' : annonces, })

# Test List View
class AnnonceListView(ListView):

    model = Annonce

    def get_context_data(self, **kwargs):
        context = super(AnnonceListView, self).get_context_data(**kwargs)
        return context

# Test DetailView
class AnnonceDetailView(DetailView):

    model = Annonce

    def get_context_data(self, **kwargs):
        context = super(AnnonceDetailView, self).get_context_data(**kwargs)
        success_url = reverse_lazy('plateforme:annonce_list')
        return context

# Actualités / Annonces / Infos
def infoAnnonces(request):
	return render(request, 'plateforme/infoAnnonces.html', {})

# Actualités / Timeline
def timeline(request):
	evenement = Evenement.objects.all()
	annonces = Annonce.objects.all()
	return render(request, 'plateforme/timeline.html', {'evenement' : evenement, 'annonces' : annonces,  })

# Education
def education(request):
	return render(request, 'plateforme/education.html', {})

# Education / Cours
def cours(request):
	return render(request, 'plateforme/cours.html', {})

# Espace Membre / Forum
def forum(request):
	themes = ThemeForum.objects.all()
	return render(request, 'plateforme/forum.html', {'themes' : themes})

# Espace Membre / Blog
def blog(request):
	return render(request, 'plateforme/blog.html', {})

# Contact
def contact(request):
	return render(request, 'plateforme/contact.html', {})

# Aide / FAQ
def faq(request):
	return render(request, 'plateforme/faq.html', {})

