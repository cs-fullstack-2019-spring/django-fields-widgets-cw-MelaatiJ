from .models import SuperHeroModel
from django import forms


# - If you have a super power, which ones? (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
ability = ( ("Flight", "Flight"),
            ("Speed", "Speed"),
            ("Invisibility", "Invisibility"),
            ("Telekenetic","Telekenetic" ),
            ("Healing","Healing"),
            ("other","other"),


)
# Which of the following are you? (Good, kinda good, neutral, a little evil, evil)
heart = (
    ("Good", "Good"),
    ("Kinda Good", " kinda Good"),
    ("Neutral", "Neutral"),
    ("A little evil", "A little Evil"),
    ("Evil", "Evil"),

)

class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHeroModel
        fields = "__all__"
        labels = {
            "fromWhere": "City or Origin ?",
            "status": "Are you rich or have super powers ?",
            "power": "If you have a super power, which ones?",
            "intention" : "Which of the following are you?",
            "examples": "Give us 3 examples of when you used your super hero abilities.",
        }
        widgets = {
            "status": forms.RadioSelect(choices=ability),
            "intention":forms.RadioSelect(choices=heart),
        }