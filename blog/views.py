import datetime

from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.http import HttpResponse,Http404
from django.utils import timezone

from blog.forms import ContactForm, NouveauContactForm
from blog.models import Article,Contact


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    # try:
    #     article = Article.objects.get(id=id)
    # except Article.DoesNotExist:
    #     raise Http404
    article = get_object_or_404(Article, id=id,slug=slug)
    return render(request, 'blog/lire.html', {'article': article})


def view_article(request,id_article):
    aa=int(id_article)
    print(type(aa))
    if aa > 100:
        print('hhhhhhhhhh')
        raise Http404
    return HttpResponse("Vous avez demandé l'article n° {0} !{1}".format(id_article,5) )


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def list_articles(request, year, month):
    # return HttpResponse("Vous avez demandé les articles de %s   ££ %s."%(month, year))
    # return redirect("https://www.djangoproject.com")
    return redirect('afficher_article',id_article=100)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': timezone.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    couleurs = {
        'FF0000': 'rouge',
        'ED7F10': 'orange',
        'FFFF00': 'jaune',
        '00FF00': 'vert',
        '0000FF': 'bleu',
        '4B0082': 'indigo',
        '660099': 'violet',
    }
    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())


def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })