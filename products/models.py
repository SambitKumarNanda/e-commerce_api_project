from django.db import models


# Create your models here.
class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductBrandModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductColorModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductDescriptionModel(models.Model):
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to="product-image/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductServiceModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    icon = models.FileField(upload_to="product-image/services/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductVariationModel(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    brand = models.ForeignKey(ProductBrandModel, on_delete=models.CASCADE, related_name="ProductModel_brand", null=True,
                              blank=True)
    images = models.ManyToManyField(ProductImageModel, related_name="ProductModel_images", blank=True)
    description = models.ManyToManyField(ProductDescriptionModel, related_name="ProductModel_description", blank=True)
    category = models.ForeignKey(ProductCategoryModel, related_name="ProductModel_category", on_delete=models.CASCADE,
                                 null=True, blank=True)
    services = models.ManyToManyField(ProductServiceModel, related_name="Product_services", blank=True)
    variation = models.ManyToManyField(ProductVariationModel, related_name="ProductModel_variation", blank=True)
    color = models.ForeignKey(ProductColorModel, on_delete=models.CASCADE, related_name="ProductModel_color", null=True,
                              blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductMainModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="ProductMainModel_product",
                                null=True, blank=True)
    product_code = models.CharField(max_length=100, unique=True, primary_key=True)
    variation = models.ForeignKey(ProductVariationModel, on_delete=models.CASCADE,
                                  related_name="ProductMainModel_variation", null=True, blank=True)
    color = models.ForeignKey(ProductColorModel, on_delete=models.CASCADE, null=True, blank=True)

    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    final_price = models.DecimalField(decimal_places=2, max_digits=10)

    is_ordered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
