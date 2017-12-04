from django.db import models
from django.contrib.auth.models import User, Permission
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.

# TEST
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()




class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')
    views = models.PositiveIntegerField(default=0)  # <- here

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))


class Evenement(models.Model):
	evenement = models.CharField(max_length=100, null=True, blank=True, verbose_name="Evenement")
	lieu = models.CharField(max_length=100, null=True, blank=True, verbose_name="Lieu")
	dateCreation = models.DateField(verbose_name="Date de l'evenement")
	jour = models.CharField(max_length=100, null=True, blank=True, verbose_name="Jour")
	mois = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mois")
	annee = models.CharField(max_length=100, null=True, blank=True, verbose_name="Année")
	heure = models.CharField(max_length=100, null=True, blank=True, verbose_name="Heure")
	hDebut = models.CharField(max_length=100, null=True, blank=True, verbose_name="Heure de Début")
	hFin = models.CharField(max_length=100, null=True, blank=True, verbose_name="Heure de Fin ")
	contact = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="Contact")
	nbreParticipants = models.IntegerField(blank=True, null=True, verbose_name=" Nbre de Participants")
	bureau = models.IntegerField(blank=True, null=True, verbose_name="Membres du Bureau présents")
	resume = models.TextField(blank=True, null=True, verbose_name="Rapport de la réunion")
	odd1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 1")
	odd2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 2")
	odd3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 3")
	odd4 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 4")
	odd5 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 5")
	odd6 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 6")
	odd7 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 7")
	odd8 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 8")
	odd9 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 9")
	odd10 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ordre du Jour 10")

	def __str__(self):
		return self.evenement

	def get_absolute_url(self):
		return reverse('plateforme:evenement-detail', kwargs={'pk': self.pk})


	class Meta:
		verbose_name_plural = 'Evenements'


class Annonce(models.Model):
	titre = models.CharField(max_length=100, null=True, blank=True, verbose_name="Titre")
	lieu = models.CharField(max_length=100, null=True, blank=True, verbose_name="Lieu")
	dateCreation = models.DateField(verbose_name="Date de l'evenement")
	jour = models.CharField(max_length=100, null=True, blank=True, verbose_name="Jour")
	mois = models.CharField(max_length=100, null=True, blank=True, verbose_name="Mois")
	annee = models.CharField(max_length=100, null=True, blank=True, verbose_name="Année")
	contact = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="Contact")
	email = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="Email")
	annonce = models.TextField(blank=True, null=True, verbose_name="Annonce")

	def __str__(self):
		return self.titre

	def get_absolute_url(self):
		return reverse('plateforme:annonce-detail', kwargs={'pk': self.pk})


	class Meta:
		verbose_name_plural = 'Annonces'


class ThemeForum(models.Model):
    titre = models.CharField(max_length=30, unique=True, verbose_name="Titre")
    description = models.CharField(max_length=100, verbose_name="Description")

    def __str__(self):
    	return self.titre

    class Meta:
    	verbose_name_plural = 'Themes_Forum'


class SujetForum(models.Model):
    sujet = models.CharField(max_length=255, verbose_name="Sujet")
    last_updated = models.DateTimeField(auto_now_add=True)
    theme = models.ForeignKey(ThemeForum, null=True, blank=True, related_name='sujetforums')
    auteur = models.ForeignKey(User, related_name='sujetforums')

    def __str__(self):
    	return self.sujet

    class Meta:
    	verbose_name_plural = 'Sujets_Forum'


class Commentaires(models.Model):
    message = models.TextField(max_length=4000)
    sujetforum = models.ForeignKey(SujetForum, related_name='commentaires')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='commentaires')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __unicode__(self):
    	return self.User.created_by

    class Meta:
    	verbose_name_plural = 'Commentaires'



