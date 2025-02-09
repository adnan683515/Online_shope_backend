from django.contrib import admin
from .models import Cart,CartItem,Order


from django.template.loader import render_to_string
from django.core.mail import  EmailMultiAlternatives


class ModelAdminOder(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        print("admin",obj.zila)
        if obj.status == 'Shipped':
            mail_sub = 'Hello Dear Customer!'
            email_body = render_to_string('status_email.html',{'mail_sub':mail_sub,"product":obj.product,'obj':obj})
            email = EmailMultiAlternatives(mail_sub,'',to=[obj.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
        if obj.status == 'Delivered':
            mail_sub = 'Hello Dear Customer!'
            email_body = render_to_string('deliverd_email.html',{'mail_sub':mail_sub,"product":obj.product,'obj':obj})
            email = EmailMultiAlternatives(mail_sub,'',to=[obj.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

admin.site.register(Cart)
admin.site.register(Order,ModelAdminOder)
admin.site.register(CartItem)


