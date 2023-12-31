from django.db import models

class News(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_publiched=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural =' Новости'
        ordering = ['created_at']
