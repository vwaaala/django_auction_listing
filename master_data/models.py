from django.db import models


class ProductGroup(models.Model):
    GROUP_CHOICES = [
        ('car', 'car'),
        ('truck', 'truck'),
        ('machine', 'machine'),
        ('other', 'other'),
    ]

    title = models.CharField(max_length=100)
    group = models.CharField(max_length=7, choices=GROUP_CHOICES, default=GROUP_CHOICES[2])

    def __str__(self):
        return self.title


class ProductSubGroup(models.Model):
    id_group = models.ForeignKey('ProductGroup', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductBrand(models.Model):
    id_group = models.ForeignKey('ProductGroup', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductBrandModel(models.Model):
    id_brand = models.ForeignKey('ProductBrand', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    id_subgroup = models.ForeignKey('ProductSubGroup', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductSubCategory(models.Model):
    id_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TechnicalState(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class FuelType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class DriveType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
