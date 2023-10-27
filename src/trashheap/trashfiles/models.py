from django.db import models
import hashlib

# Create your models here.
class TrashFile(models.Model):
    # create an id field that allows for a blake3 hash
    id = models.CharField(max_length=64, primary_key=True)
    filenames = models.TextField()
    filepaths = models.TextField()
    filetypes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Trash Files"

