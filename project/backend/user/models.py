from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password = None):
        if not email:
            raise ValueError("user must have an email address")

        if not username:
            raise ValueError("User must have username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
           
        )
        user.is_active = True
        user.set_password(password)
        user.save(using= self._db)
        return user   
    
    def create_superuser(self, first_name,last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name =last_name,
        )
        user.is_admin =True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    username =  models.CharField(max_length=50 , unique = True)
    email = models.EmailField(max_length=100 , unique=True)
    Phone_number = models.CharField(max_length=50,null = True, blank=True)
    Task = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    Point = models.IntegerField(validators=[MinValueValidator(0)], default=0)


    #required

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin =  models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    is_superadmin =  models.BooleanField(default=False)


     
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True



class Profile(models.Model):
    User = models.ForeignKey(Account,on_delete=models.CASCADE)
   



class App(models.Model):
    STATUS = (
        ('App', 'App'),
        ('Games', 'Games'),
    )
    SELECT = (
        ('Social_Media', 'Social_Media'),
        ('Music', 'Music'),
        ('Film', 'Film'),
    )
    Appname = models.CharField(max_length=50 , unique = True)
    Applink = models.CharField(max_length=300)
    Category = models.CharField(max_length=40, choices=STATUS, default='')
    SubCategory = models.CharField(max_length=40, choices=SELECT, default='')
    Point =  models.IntegerField(validators=[MinValueValidator(0)], default=0)



class Task(models.Model):
    User =  models.ForeignKey(Account,on_delete=models.CASCADE)
    Appname = models.CharField(max_length=100, default='')
    Point =  models.IntegerField(default=0)
    AppId =  models.IntegerField(default=0)

