from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=20)

    @property
    def movie_count(self):
        return self.movie_set.count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    duration = models.FloatField()
    directors = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        total_stars = sum(review.stars for review in self.review_set.all() if review.stars is not None)
        total_reviews = self.review_set.exclude(stars=None).count()

        if total_reviews > 0:
            return total_stars / total_reviews
        else:
            return 0


class Review(models.Model):
    STATUS_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    stars = models.IntegerField(choices=STATUS_CHOICES, null=True, default=None)

    def rating(self):
        return self.stars

    def __str__(self):
        return self.text
