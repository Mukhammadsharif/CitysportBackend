from django.db import models


class Pool(models.Model):
    name = models.CharField(max_length=100)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Billiard(models.Model):
    name = models.CharField(max_length=100)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Sauna(models.Model):
    name = models.CharField(max_length=100)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    subscription_date = models.DateField()
    expiration_date = models.DateField()
    phone = models.CharField(max_length=20)
    debt = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    TYPE_CHOICES = (
        ('billiard', 'Billiard'),
        ('pool', 'Pool'),
        ('training', 'Training'),
        ('sauna', 'Sauna'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    number = models.IntegerField()
    date_entered = models.DateTimeField()
    date_exit = models.DateTimeField()
    summ = models.CharField(max_length=50)
    relax = models.BooleanField()
    phone = models.CharField(max_length=15)
    additional_info = models.TextField(blank=True)
    shorts_number = models.IntegerField()
    is_subscribed = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    debt = models.CharField(max_length=50)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=True, blank=True)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, null=True, blank=True)
    billiard = models.ForeignKey(Billiard, on_delete=models.CASCADE, null=True, blank=True)
    sauna = models.ForeignKey(Sauna, on_delete=models.CASCADE, null=True, blank=True)
    training = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Order {self.id}"


class Notification(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
