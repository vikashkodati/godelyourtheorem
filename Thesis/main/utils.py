'''
Created on Jan 30, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''
from django.db import models
from django.contrib.auth.models import User

class ResultUser(object):
    username = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    location = models.CharField()
    
    def __init__(self, user_profile, user):
        username = user.username
        first_name = user.first_name
        last_name = user.last_name
        location = user_profile.location