from django.db import models

class WordFiles(models.Model):
    Title=models.TextField()
    Description=models.TextField()
    def __str__(self):
	       return self.Title+" "+self.Description+" "

class WordFiles_Attachment(models.Model):
    key = models.ForeignKey(WordFiles,on_delete=models.CASCADE)
    file = models.TextField( null=True, blank=True)
