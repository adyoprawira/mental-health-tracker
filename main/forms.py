from django.forms import ModelForm
from main.models import MoodEntry
from django.utils.html import strip_tags

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry   # Indicates the model to be used
        fields = ["mood", "feelings", "mood_intensity"] # Indicate the fields of the model
    def clean_mood(self):
        mood = self.cleaned_data["mood"]
        return strip_tags(mood)

    def clean_feelings(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)