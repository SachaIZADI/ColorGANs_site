from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import requests
# import StringIO

from django.core.files.uploadedfile import InMemoryUploadedFile
import base64


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        # # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # # fs.
        # filename = fs.save(myfile.name, myfile)
        # # print(filename)
        # uploaded_file_url = fs.url(filename)
        # # print(uploaded_file_url)
        # return render(request, 'core/make_magic.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
        # ================================================
        # myfile = request.FILES['myfile']
        # r = requests.post('http://127.0.0.1:5000/predict', files={'image': myfile})
        # return render(request, 'core/simple_upload_sacha_predict.html', {
        #     'uploaded_file_url': r.text
        # })
        # ================================================
        myfile = request.FILES['myfile']
        r = requests.post('http://127.0.0.1:5000/return_image', files={'image': myfile})
        from PIL import Image
        import io
        image2 = r.content
        image2 = Image.open(io.BytesIO(image2))
        image2.save("media/GANImage", format='PNG')

        return render(request, 'core/simple_upload_sacha_predict.html', {
            'uploaded_file': image
            # 'url_to_image': image_url
        })
    return render(request, 'core/simple_upload.html')

    ################################ Sacha's stuff #########################################


# @Valentin : cette fonction c'est juste pour tester que je peux prendre une image et la passer dans mon neural net
def simple_upload_sacha_predict(request):
    if request.method == 'POST' and request.FILES['myfile']:
        # @Valentin : la je garde uniquement le fichier en memoire (je ne le download pas dans le dossier media). Je t'expliquerai pourquoi demain ...
        myfile = request.FILES['myfile']

        # @Valentin : la je fais une requete sur mon API flask (l'url sera differente quand j'aurais cree l'api sur GoogleCloud)
        r = requests.post('http://127.0.0.1:5000/predict', files={'image': myfile})

        # @Valentin : r.text = le resultat de mon classifier
        return render(request, 'core/simple_upload_sacha_predict.html', {
            'uploaded_file_url': r.text
        })
    return render(request, 'core/simple_upload.html')



#@ Valentin : cette fonction c'est pour voir que je peux envoyer une image dans mon api et recuperer une image derriere
def simple_upload_sacha_return_image(request):
    if request.method == 'POST' and request.FILES['myfile']:
        # @Valentin : la je garde uniquement le fichier en memoire
        myfile = request.FILES['myfile']
        r = requests.post('http://127.0.0.1:5000/return_image', files={'image': myfile})

        # @Valentin : r.content =  l'image que j'ai genere, j'utilise PIL.Image pour bien gerer l'image
        from PIL import Image
        import io
        image = r.content
        image = Image.open(io.BytesIO(image))


        #TODO : @Valentin, maintenant que j'ai l'image en memoire, il faudrait que tu puisses l'afficher dans le site web stp :)

        return render(request, 'core/simple_upload_sacha_predict.html', {
            'uploaded_file_url': image
        })
    return render(request, 'core/simple_upload.html')



#####################################################################################


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def description(request):
    return render(request, "core/description.html")

def us(request):
    return render(request, "core/us.html")

def templates(request):
    return render(request, "core/templates.html")

def refs(request):
    return render(request, "core/refs.html")
