from django.db import models

# Create your models here.
class Main(models.Model):
    photo = models.ImageField(upload_to='media/',null=True,blank=True)
    text1 =models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    text3 = models.TextField()


    def __str__(self):
        return self.text1
    
class Welcome(models.Model):
    text1 = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.text1
    
class Slider(models.Model):
    CATEGORY={
        ("Business Law","Business Law"),
        ("Family Law","Family Law"),
        ("Criminal Law","Criminal Law"),
        
    }
    photo = models.ImageField(upload_to='media/')
    category = models.CharField(choices=CATEGORY ,default="Business Law" ,max_length=100)
    text = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class BigPhoto(models.Model):
    image = models.ImageField(upload_to='media/asosiy/')

    def __str__(self):
        return str(self.id)
    
class BigSlide(models.Model):
    CATEGORY={
        ("Business Law","Business Law"),
        ("Family Law","Family Law"),
        ("Criminal Law","Criminal Law"),
        
    }
    category = models.CharField(choices=CATEGORY,default="Business Law",max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.category

class Stat(models.Model):
    number = models.CharField(max_length=1000)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
class Team(models.Model):
    photo = models.ImageField(upload_to='media/team/')
    name = models.CharField(max_length=100)
    staff = models.CharField(max_length=100)
    insta = models.CharField(max_length=500)
    telegram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=300)
    linkedn = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    
class Comments(models.Model):
     CATE={
        ("Baddies","Baddies"),
        ("Goodies","Goodies"),
    }
     
     text = models.TextField()
     name = models.CharField(max_length=100)
    #  orign = models.CharField(max_length=100)
     category = models.CharField(choices=CATE,default='Goodies' ,max_length=100)
     def __str__(self):
         return self.name

class Bloging(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='media/blog')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    like = models.IntegerField()

    def __str__(self):
        return self.name

class Izoh(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    update_data=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Contacpage(models.Model):
    photo= models.ImageField(upload_to='media/contct/')
    title =models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
     
    def __str__(self):
        return self.title 
   
   
class Message(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    text=models.TextField()
    phone=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
    update_data=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
class AboutSlide(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    number=models.IntegerField()
    photo1=models.ImageField(upload_to='media/about/')
    photo2=models.ImageField(upload_to='media/about/')
    
    def __str__(self):
        return self.title 
    

class Experience(models.Model):
    name=models.CharField(max_length=100) 
    title=models.CharField(max_length=100)
    text=models.TextField()
    number=models.IntegerField()
    title2=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
class News (models.Model):
    photo=models.ImageField(upload_to='media/news')
    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    text=models.TextField()
    link=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    