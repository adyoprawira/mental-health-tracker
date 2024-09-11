from django.forms import ModelForm
from main.models import MoodEntry

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry   # Indicates the model to be used
        fields = ["mood", "feelings", "mood_intensity"] # Indicate the fields of the model