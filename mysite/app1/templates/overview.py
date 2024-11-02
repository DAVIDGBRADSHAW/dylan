class Post(models.Model):
    title = models.VharField(max_length)
    content = models.TextField()
    date_posted =  models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)