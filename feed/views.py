from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def index(request):
    """Home page for feed."""
    images = Image.objects.all().order_by('-uploaded_at')
    return render(request, 'feed/index.html')

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ImageForm()
#     return render(request, 'feed/upload_image.html', {'form': form})
