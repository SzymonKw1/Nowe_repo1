from django.contrib import admin
from .models import Team, Person, Stanowisko, Osoba

admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Stanowisko)


# Register your models here.
class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description= "Stanowisko (ID)")
    def stanowisko_with_id(self, obj):
        if obj.stanowisko :
            return f'{obj.stanowisko} ({obj.stanowisko.id})'
        return 'Brak stanowiska'
    list_display =["imie", "nazwisko", "plec", "stanowisko_with_id", "data_dodania"]

admin.site.register(Osoba, OsobaAdmin)