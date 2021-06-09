from .models import Home,Blogpost
import datetime

def Author(request):
    try:
        name = Home.objects.values('name')[0]['name']
        author = Home.objects.get(name=name)
        return {'author':author}
    except Exception:
        author = ''
        return {'author':author}
    

def TrandingAndPopularPost(request):
    week_ago = datetime.date.today() - datetime.timedelta(days = 7)
    tranding = Blogpost.objects.filter(posttime__gte = week_ago).order_by('-read')
    popularPost = Blogpost.objects.order_by('-read')
    return {'tranding':tranding[:3], 'popularPost':popularPost[:3]}