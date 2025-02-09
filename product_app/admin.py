from django.contrib import admin
from .models import Product,size,review,range_of_price,cetagory,colour,favorites,country,view_model,Brand
from .models import warenty,Movement_Watch,TypeOFJacket
# Register your models here.


admin.site.register(warenty)
admin.site.register(Movement_Watch)
admin.site.register(cetagory)
admin.site.register(Product)
admin.site.register(review)
admin.site.register(size)
admin.site.register(range_of_price)
admin.site.register(colour)
admin.site.register(favorites)
admin.site.register(country)                                                   
admin.site.register(view_model)          
admin.site.register(Brand)  



from .models import Team,version,MainMetariails

admin.site.register(Team)
admin.site.register(version)
admin.site.register(MainMetariails)

admin.site.register(TypeOFJacket)
