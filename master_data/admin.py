from django.contrib import admin

from master_data.models import ProductGroup, ProductSubGroup, ProductBrand, ProductBrandModel, ProductCategory, \
    ProductSubCategory, TechnicalState

admin.site.register(ProductGroup)
admin.site.register(ProductSubGroup)
admin.site.register(ProductBrand)
admin.site.register(ProductBrandModel)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(TechnicalState)
