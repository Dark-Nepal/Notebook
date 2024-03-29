from datetime import datetime


from django.shortcuts import render, get_object_or_404

from .forms import AddForm
from .models import DiaryModel
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'signin')
def entry(request):
    form = AddForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            note = request.POST['note']
            content = request.POST['content']
            posted_date = datetime.now()
            productivity = request.POST['productivity']

            todays_diary = DiaryModel()
            todays_diary.author = request.user
            todays_diary.note = note
            todays_diary.posted_date = posted_date
            todays_diary.content = content
            todays_diary.productivity = productivity

            todays_diary.save()

           

        """
            Clear the form and return.
           
        """
        return render(
        request,
        'entry/add.html',
        {
            'title': 'Message!!',
            'subtitle': ' Successfully diary of today is save.',
            'add_highlight': True,
            'addform': form,
        }
    )

    return render(
        request,
        'entry/add.html',
        {
            'title': 'Add Entry',
            'subtitle': 'Add what you feel and we\'ll store it for you.',
            'add_highlight': True,
            'addform': form,
        }
    )

@login_required(login_url = 'signin')
def show(request):
    """
        We need to show the diaries sorted by date posted in descending order
        
    """
    diaries = DiaryModel.objects.order_by('posted_date').filter(author=request.user)
    icon = True if len(diaries) == 0 else None

    return render(
        request,
        'entry/show.html',
        {
            'show_highlight': True,
            'title': 'All Entries',
            'subtitle': 'It\'s all you\'ve written.',
            'diaries': reversed(diaries),
            'icon': icon
        }
    )

@login_required(login_url = 'signin')
def detail(request, diary_id):
    diary = get_object_or_404(DiaryModel, pk=diary_id)

    return render(
        request,
        'entry/detail.html',
        {
            'show_highlight': True,
            'title': diary.note,
            'subtitle': diary.posted_date,
            'diary': diary
        }
    )

@login_required(login_url = 'signin')
def productivity(request):
    
    """
        At max, draw chart for last 10 data.

    """
    data = DiaryModel.objects.order_by('posted_date')[:10]
    icon = True if len(data) == 0 else None

    return render(
        request,
        'entry/productivity.html',
        {
            'title': 'Productivity Chart',
            'subtitle': 'Keep the line heading up always.',
            'data': data,
            'icon': icon
        }
    )
