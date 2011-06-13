from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
import datetime
import models
import forms
import lib

def new(request):
    form = forms.MeetingForm(data=request.POST)
    data= {'form': form}

    if request.method == 'POST':

        form = forms.MeetingForm(data=request.POST)
        meeting = models.Meeting()
        valid = False

        #routine meeting?
        if not request.POST.get('routine', False):
            if form.is_valid():
                meeting = form.save(commit=False)
                valid = True
        else:
            #standup
            if request.POST.get('routine-standup', False):
                meeting.title ="Standup - "+ datetime.date.today().strftime("%B %d, %Y")
                meeting.purpose ="Daily team catchup"
                meeting.length_in_minutes = 15
                valid = True
            #show and tell
            if request.POST.get('routine-showandtell', False):
                meeting.title ="Show and tell - " + datetime.date.today().strftime("%B %d, %Y")
                meeting.purpose ="Show the output for the current sprint"
                meeting.length_in_minutes = 60
                valid = True

        if valid:
            meeting.etherpad_url = lib.get_etherpad_url()
            meeting.save()

            #off to the meeting page!
            return HttpResponseRedirect(reverse('meeting', args=(meeting.id,)))

    return render_to_response('new.html', data, context_instance = RequestContext(request))

def meeting(request, meeting_id):
    meeting = get_object_or_404(models.Meeting, id=meeting_id)
    offset_seconds = 0
    if datetime.datetime.now() > meeting.date_time_started:
        offset_seconds = (datetime.datetime.now() - meeting.date_time_started).seconds

    data = {'meeting':meeting, 'offset_seconds': offset_seconds}
    return render_to_response('meeting.html', data, context_instance = RequestContext(request))

def all(request):
    meetings = models.Meeting.objects.all().order_by('-date_time_started')
    data = {'meetings':meetings,}
    return render_to_response('all.html', data, context_instance = RequestContext(request))    
