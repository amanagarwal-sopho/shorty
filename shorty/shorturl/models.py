from django.db import models

import random
import string

class URLEntry(models.Model):
    code = models.CharField(max_length=8)
    url = models.URLField(max_length=500)
    
    class Meta:
        verbose_name = 'URL Entry'
        verbose_name_plural = 'URL Entries'
        
        
    def create_code(self):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.code = ''.join([random.choice(letters) for i in range(8)])
        self.save()
        return self
        
        
        

        
