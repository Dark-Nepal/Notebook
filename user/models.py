from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager





class UserManager(BaseUserManager):

   def create_user(self, first_name, last_name, username, email, password=None ):
       if not email:
           raise ValueError('Use must have email')
   
       if not username:
           raise ValueError('User must have username') 
   
       '''
       Creating User in movies application
   
       author:DarkNepal 
       
       '''
       user = self.model(
           email = self.normalize_email(email),
           username = username,
           password   = password,
           first_name = first_name,
           last_name = last_name
       )
   
       # Setting Password for user
   
       user.set_password(password)
       user.save(using=self._db)
       return user


   def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password   = password,
            first_name = first_name,
            last_name = last_name,
        )

                                       
        user.is_admin      = True
        user.is_staff      = True
        user.is_active     = True
        user.is_superuser  = True
        user.save(using=self._db)

        return user




class User(AbstractBaseUser):

    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name  = models.CharField(max_length=100, verbose_name='Last Name')
    email      = models.EmailField(unique=True,verbose_name='Email')
    username   = models.CharField(max_length=50, unique=True, verbose_name='Username')
    phone      = models.CharField(max_length=20, verbose_name='Phone number')

    #required
    joined_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Joined Date')
    last_login = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Last Login')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [ 'first_name', 'last_name', 'username']
    
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        full_name = (self.first_name + self.last_name)
        return full_name
    
    
     
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    