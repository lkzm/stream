from django.shortcuts import render
import models, forms
# Create your views here.
def upload_track(request):
    form = forms.UploadSetForm(request.POST, request.FILES)
    context = {
            'form' : form,
            }
    if form.is_valid():

        f = form.cleaned_data['set']

        s = models.Set.objects.create(
                file = f
                )
        return set(request, s.pk)
    else:
        return render(request, 'sound/store/upload_set.html', context)
    return render(request, 'sound/store/upload_set.html', context)


def set (request, set_id):
    s = models.Set.objects.get(pk=set_id)
    context = {
        'id' : s.pk,
        'file': s.file.path,
    }
    return render (request, 'sound/store/set_id.html', context)



def upload_vid(request):
    form = forms.UploadVidForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    if form.is_valid():

        f = form.cleaned_data['set']

        v = models.Set.objects.create(
            file=f
        )
        return vid(request, v.pk)
    else:
        return render(request, 'sound/store/upload_vid.html', context)
    return render(request, 'sound/store/upload_vid.html', context)
def vid (request, vid_id):
    v = models.Set.objects.get(pk=vid_id)
    context = {
        'id' : v.pk,
        'file': v.file.path,
    }
    return render (request, 'sound/store/set_id.html', context)