from django.forms import ModelForm
from .models import Skill, Note

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['description', 'skill_level']

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['content']
