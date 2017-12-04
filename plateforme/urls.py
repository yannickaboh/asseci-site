from django.conf.urls import url, include
from django.contrib import admin
from plateforme import views
from . import views
from .views import EvenementListView, EvenementDetailView, AnnonceListView, AnnonceDetailView

from accounts import views as accounts_views

from django.contrib.auth import views as auth_views

app_name = 'plateforme'



urlpatterns = [

    # TEST
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='plateforme/login.html'), name='login'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^new_post/$', views.NewPostView.as_view(), name='new_post'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='plateforme/password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='plateforme/password_change_done.html'),
        name='password_change_done'),

    url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='plateforme/password_reset.html',
        email_template_name='plateforme/password_reset_email.html',
        subject_template_name='plateforme/password_reset_subject.txt'
    ),
    name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='plateforme/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='plateforme/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='plateforme/password_reset_complete.html'),
        name='password_reset_complete'),



    url(r'^admin/', admin.site.urls),

    # Inscription
    url(r'^inscription/$', views.inscription, name='inscription'),

    # Connexion
    url(r'^connexion/$', views.connexion, name='connexion'),

    # Mot de passe oublié
    url(r'^mot-de-passe-oublie/$', views.forgotpassword, name='forgotpassword'),

    # Mentions Légales
    url(r'^mentions-legales/$', views.mentionslegales, name='mentionslegales'),

    # Paiement en ligne
    url(r'^paiement-en-ligne/$', views.paiement, name='paiement'),

    # Plan du Site
    url(r'^plan-du-site/$', views.plan, name='plan'),

    # Accueil
    url(r'^accueil/$', views.accueil, name='accueil'),

    # Présentation
    url(r'^presentation/$', views.presentation, name='presentation'),

    # Présentation / Missions
    url(r'^presentation/nos-missions/$', views.missions, name='missions'),

    # Présentation / Bureau
    url(r'^presentation/bureau/$', views.bureau, name='bureau'),

    # Profil
    url(r'^promotions/id/$', views.profil, name='profil'),

    # Profil / Membre / Id
    url(r'^promotion/membre/id/profil/$', views.profileId, name='profileId'),

    # Profil / Membre / CV
    url(r'^promotion/membre/id/CV/$', views.profileCv, name='profileCv'),

    # Actualités
    url(r'^actualites/$', views.actualites, name='actualites'),

    # Actualités / Evenements
    url(r'^actualites/evenements/$', views.evenements, name='evenements'),

    # Test Actualités
    # Add, Update, Delete Evenement URLS
    url(r'^actualites/evenement_list/$', EvenementListView.as_view(), name='evenement-list'),
    url(r'^actualites/evenement/(?P<pk>\d+)/$', EvenementDetailView.as_view(), name='evenement-detail'),

    url(r'^actualites/annonce_list/$', AnnonceListView.as_view(), name='annonce-list'),
    url(r'^actualites/annonce/(?P<pk>\d+)/$', AnnonceDetailView.as_view(), name='annonce-detail'),
    #url(r'^evenement_list/$', views.EvenementList.as_view(), name='evenement_list'),
    #url(r'^evenement_create/$', views.EvenementCreate.as_view(), name='evenement_create'),
    #url(r'^evenement_detail/$', views.EvenementDetail.as_view(), name='evenement_detail'),
    #url(r'^evenement_update/(?P<pk>\d+)/$', views.EvenementUpdate.as_view(), name='evenement_update'),
    #url(r'^evenement_delete/(?P<pk>\d+)/$', views.EvenementDelete.as_view(), name='evenement_delete'),

    # Actualités / Evenements / Infos
    url(r'^actualites/evenements/id/infos/$', views.infoEvenements, name='infoEvenements'),

    # Actualités / Annonces
    url(r'^actualites/annonces/$', views.annonces, name='annonces'),

    # Actualités / Annonces / Infos
    url(r'^actualites/annonces/id/infos/$', views.infoAnnonces, name='infoAnnonces'),

    # Actualités / Timeline
    url(r'^actualites/timeline/$', views.timeline, name='timeline'),

    # Education
    url(r'^education/$', views.education, name='education'),

    # Education / Cours
    url(r'^education/cours/$', views.cours, name='cours'),

    # Forum
    url(r'^forum/$', views.forum, name='forum'),

    # Blog
    url(r'^blog/$', views.blog, name='blog'),

    # FAQ
    url(r'^faq/$', views.faq, name='faq'),

    # Contact
    url(r'^contact/$', views.contact, name='contact'),
]