from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']  # Сортировка по юникоду
        unique_together = (
            (
                "name",
                "duration",
                "price",
            )
        )

        def __str__(self):
            return self.name
