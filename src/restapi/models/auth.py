#from django.contrib.auth.models import (
 #	BaseUserManager, 
  #  AbstractBaseUser
#)
#from django.db import models

#class UserManager(BaseUserManager):
 #  def create_user(self, email, password=None,**extra_fields):
   #     """
   #     Creates and saves a User with the given email and password.
   #     """
  #      if not email:
   #         raise ValueError('Users must have an email address')

    #    user = self.model(
     #       email=self.normalize_email(email),**extra_fields
      #  )

       # user.set_password(password)
       # user.save(using=self._db)
       # return user

#class User(AbstractBaseUser):
 #   email = models.EmailField(max_length=255,unique=True)
  #  firstname = models.TextField(blank=False)
   # lastname = models.TextField(blank=True)
    #is_active = models.BooleanField(default=True)

    #objects = UserManager()
    #USERNAME_FIELD = 'email'
    
    #class Meta:
     #   db_table = 'User'


