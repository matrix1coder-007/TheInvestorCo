from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid

# Create your models here.
# Time-stamp model
class TimestampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Custom User Base Manager
class CustomUserBaseManager(BaseUserManager):

    def create_user(self, user_fname, user_mname, user_lname, user_email, password=None):

        # user name requirements
        if not user_fname:
            raise ValueError("Users must have a first name.")
        if not user_lname:
            raise ValueError("Users must have a last name.")

        # user e-mail requirements 
        if not user_email:
            raise ValueError("Users must have an e-mail address.")

        user_email = self.normalize_email(user_email)
        user_instance = self.model(user_fname=user_fname, user_mname=user_mname,
            user_lname=user_lname, user_email=user_email, is_superuser=False, is_customer=True)
        user_instance.set_password(password)
        user_instance.save(using=self._db)
        return user_instance

    def create_superuser(self, user_fname, user_lname, user_email, user_mname='', password=None):

        # super-user name requirements
        if not user_fname:
            raise ValueError("Users must have a first name.")
        if not user_lname:
            raise ValueError("Users must have a last name.")

        # super-user e-mail requirements 
        if not user_email:
            raise ValueError("Users must have an e-mail address.")

        superuser_email = self.normalize_email(user_email)
        superuser_instance = self.model(user_fname=user_fname, user_mname=user_mname, 
            user_lname=user_lname, user_email=user_email, is_superuser=True, is_customer=True)
        superuser_instance.set_password(password)
        superuser_instance.save(using=self._db)
        return superuser_instance


# Custom user model
class CustomUserModel(AbstractBaseUser):

    # user personal information
    user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="pkey_user")
    user_fname = models.CharField(max_length=100, verbose_name="First Name")
    user_mname = models.CharField(max_length=100, null=True, blank=True, verbose_name="Middle Name")
    user_lname = models.CharField(max_length=100, null=True, blank=True, verbose_name="Last Name")
    user_email = models.EmailField(max_length=200, unique=True, verbose_name="User Registration E-Mail")

    # user registration information
    user_registered = models.BooleanField(default=True, verbose_name="Is Active")
    user_deactivation_dt = models.DateTimeField(null=True, blank=True, verbose_name="Deactivation Date")

    # user type
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)


    objects = CustomUserBaseManager()

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_fname", "user_lname"]

    # model methods
    def __str__(self):
        return self.user_email

    # user full name
    def full_name(self):
        midname = self.user_mname if self.user_mname else " "
        return self.user_fname + " " + midname + " " + self.user_lname

    # user registered e-mail
    def registered_email(self):
        return self.user_email

    # user registration status
    def registration_status(self):
        if self.user_registration_email_sent and not self.user_registered:
            return "Registration E-mail sent.. No response received yet."
        elif self.user_registration_email_sent and self.user_registered:
            return "Registration is complete."


    # user has permissions
    def has_perm(self, perm, obj=None):
        return True


    # user has module permissions
    def has_module_perms(self, app_label):
        return True


    class Meta:
        abstract = False
        db_table = "Custom_User"
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

