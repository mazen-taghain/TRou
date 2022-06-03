from django.db import models

# Create your models here.
class User(BaseUserManager):
    def create_user(self, Email, FullName=None, Location=None, Address=None, Password=None):
        if not Email:
            raise ValueError('This Mail not Found')
        user = self.model(
            Email_Address = self.normalize_email(Email),
            Name = self.normailze_email(Email),
            Location = Location,
            Address = Address,
        )

        user.set_password(Password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, Email_Address, Password):
        user = self.create_user(
            Email_Address=self.normalize_email(Email_Address), Password=Password,
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
    

class Users(AbstractBaseUser):
    Email = models.EmailField(verbose_name="Email", max_length=60, unique=True, blank=True, null=True, default=None)
    FullName = models.CharField(max_length=30, blank=True, null=True)
    Location = models.CharField(max_length=15, blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_super_employee = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Email'

    objects = User()


    class Meta:
        db_table = "user"

    def __str__(self):
        return str(self.Email)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

