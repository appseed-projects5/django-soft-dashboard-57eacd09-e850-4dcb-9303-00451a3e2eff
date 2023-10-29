# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Coles (models.Model):

    #__Coles _FIELDS__
    product = models.CharField(max_length=255, null=True, blank=True)
    purchase_unit  = models.CharField(max_length=255, null=True, blank=True)
    recipe_unit = models.CharField(max_length=255, null=True, blank=True)

    #__Coles _FIELDS__END

    class Meta:
        verbose_name        = _("Coles ")
        verbose_name_plural = _("Coles ")



#__MODELS__END
