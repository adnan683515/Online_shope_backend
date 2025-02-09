from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

################################### GEANS ###############################################
class range_of_price(models.Model):
    price_name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.price_name
    
class country(models.Model):
    country_name = models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        ordering = ['-country_name']
    
    def __str__(self):
        return self.country_name
    
class Movement_Watch(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
type_warrenty = [
    ('jacket','jacket'),
    ('watch','watch'),
    ('powder','powder'),
    ('Football','Football'),
    ('Geans','Geans'),
    ('Saree','Saree'),
    ('Shirt','Shirt')
] 
class warenty(models.Model):
    choice_type = models.CharField(choices=type_warrenty,null=True,blank=True,max_length=1000)
    name = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
type_brand = [
    ('geans','geans'),
    ('jacket','jacket'),
    ('Saree','Saree'),
    ('Shirt','Shirt'),
    ('Watch','Watch'),
    ('Cricket Bat','Cricket Bat'),
    ('Football','Football')
]  
class Brand(models.Model):
    choice = models.CharField(choices=type_brand,null=True,blank=True,max_length=100)
    name = models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return f'${self.name} {self.choice}'  
    
class colour(models.Model):
    colour_name = models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        ordering = ['-colour_name']
    def __str__(self):
        return self.colour_name
    
type_size = [
    ('Geans','Geans'),
    ('Saree','Saree'),
    ('Jacket','Jacket'),
    ('Watch','Watch'),
    ('Bat Size','Bat Size'),
    ('Shirt','Shirt'),
    ('Powder','Powder'),
    ('Jursey','Jursey')
]
class size(models.Model):
    choice_size = models.CharField(choices=type_size,max_length=100,null=True,blank=True)
    size_name = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.size_name

choices_cetagory_type = [
    ('Shirt','Shirt'),
    ('Saree','Saree'),
    ('Geans','Geans'),
    ('Football','Football'),
    ('Powder','Powder'),
    ('Cricket Bat','Cricket Bat'),
    ('Watch','Watch')
]

class cetagory(models.Model):
    cetagorytype=models.CharField(choices=choices_cetagory_type,null=True,blank=True,max_length=100)
    name = models.CharField(max_length=100)
    datetime_a = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name
    


class TypeOFJacket(models.Model):
    
    name = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    

    
product_choice = [
    ('Saree','Saree'),
    ('Geans','Geans'),
    ('Shirt','Shirt'),
    ('T shirt','T shirt'),
    ('Watch','Watch'),
    ('Powder','Powder'),
    ('Shoo','Shoo'),
    ('Sports','Sports'),
    ('Jacket','Jacket')
]



Type = [
    ('Football','Football'),
    ('Cricket Ball','Cricket Ball'),
    ('Cricket Bat','Cricket Bat'),
    ('Jursi','Jursi'),
    ('Boot','Boot'),
    ('Basketball','Basketball'),
    ('Baseball','Baseball'),
    ('Tennis ball','Tennis ball'),
    ('Handball','Handball'),
    ('Rink Ball','Rink ball'),
    ('Volleyball ball','Volleyball ball')
    
]

class Team(models.Model):
    name= models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name

class version(models.Model):
    name  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

type_materiails = [
    ('jacket','jacket'),
    ('Bat','Bat'),
    ('jursey','jursey'),
    ('geans','geans'),
    ('watch','watch'),
    ('Saree','Saree'),
    ('Football','Football')
]

class MainMetariails(models.Model):
    choice_option = models.CharField(choices=type_materiails,max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    type_your_product = models.CharField(choices=product_choice,null=True,blank=True,max_length=100)
    TypeOFJacket = models.ForeignKey(TypeOFJacket,on_delete=models.CASCADE,null=True,blank=True)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    cetagory = models.ForeignKey(cetagory,on_delete=models.CASCADE,null=True,blank=True)
    sports_Type = models.CharField(choices=Type,null=True,blank=True,max_length=100)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True,max_length=100)
    version = models.ForeignKey(version,on_delete=models.CASCADE,null=True,blank=True)
    product_title = models.CharField(max_length=100,null=True,blank=True)
    display_image = CloudinaryField('image',null=True,blank=True)
    font_image = CloudinaryField('image',null=True,blank=True)
    quantity = models.IntegerField()
    range_of_price = models.ForeignKey(range_of_price,on_delete=models.CASCADE,null=True,blank=True)
    fixed_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    colour = models.ForeignKey(colour,on_delete=models.CASCADE,null=True,blank=True)
    country = models.ForeignKey(country,on_delete=models.CASCADE,null=True,blank=True)
    MainMetariails = models.ForeignKey(MainMetariails,on_delete=models.CASCADE,null=True,blank=True)
    size = models.ForeignKey(size,on_delete=models.CASCADE,null=True,blank=True)
    warenty = models.ForeignKey(warenty,on_delete=models.CASCADE,null=True,blank=True)
    Movement_Watch = models.ForeignKey(Movement_Watch,on_delete=models.CASCADE,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    abailable = models.CharField(max_length=100,null=True,blank=True,default='is Stock')
    eyes = models.IntegerField(default=0, null=True,blank=True)
    
    def __str__(self):
        return f'{self.fixed_price}'
    
    

class favorites(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    fav = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} {self.Product.product_title}'
    


football_rating = [
    ('⚽','⚽'),
    ('⚽⚽','⚽⚽'),
    ('⚽⚽⚽','⚽⚽⚽'),
    ('⚽⚽⚽⚽','⚽⚽⚽⚽'),
    ('⚽⚽⚽⚽⚽','⚽⚽⚽⚽⚽')
]

rating=[
    ('🧡','🧡'),
    ('🧡💚','🧡💚'),
    ('🧡💚🖤','🧡💚🖤'),
    ('💙💚💛🧡','💙💚💛🧡'),
    ('💙💚💛🧡💜','💙💚💛🧡💜')
]

class review(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    review_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.CharField(choices=rating,null=True,blank=True,max_length=100)
    football_rating = models.CharField(choices=football_rating,null=True,blank=True,max_length=100)
    
    class Meta:
        ordering = ['-review_date','-rating']  # Default ordering by price (ascending)

    def __str__(self):
        return self.Product.product_title
    
########################################################################################   
class view_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    view = models.BooleanField(default=False)
    date= models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
    class Meta:
        ordering = ['-date'] 




