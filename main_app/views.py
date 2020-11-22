from django.shortcuts import render, redirect
from .models import Skill, Note
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .forms import SkillForm, NoteForm

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def skill_index(request):
    skills = request.user.skill_set.all()
     # You could also retrieve the logged in user's kicks like this:
    # skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills/index.html', {'skills':skills})

def skill_detail(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    note_form = NoteForm()
    notes = Note.objects.filter(skill__id=skill_id)
    return render(request, 'skills/detail.html', {
      'skill':skill,
      'note_form':note_form,
      'notes':notes
      })

def new_skill(request):
  skill_form = SkillForm()
  return render(request, 'main_app/new_skill.html', {'skill_form':skill_form})

class SkillCreate(CreateView):
    model = Skill
    form_class = SkillForm
    success_url = '/index'

      # This inherited method is called when a
    # valid skills form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the skill
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class SkillDelete(DeleteView):
    model = Skill
    success_url = '/index'

class SkillUpdate(UpdateView):
  model = Skill
  fields = ['description', 'skill_level']

def add_note(request, skill_id):
  # create a ModelForm instance using the data in request.POST
  form = NoteForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the skill_id assigned
    new_note = form.save(commit=False)
    new_note.skill_id = skill_id
    new_note.save()
  return redirect('detail', skill_id=skill_id)

class NoteDelete(DeleteView):
  model = Note
  success_url = '/index'  #supposed to be going back to detail page!