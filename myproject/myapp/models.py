# from django.db import models

# # Create your models here.
# from django.contrib.postgres.fields import JSONField, ArrayField

# class Categorie(models.Model):
#     """Model definition for Categorie."""

#     # TODO: Define fields here
#     nom = models.CharField(max_length=255,null=True)
#     url_key = models.CharField(max_length=255,null=True)
#     lien = models.URLField(max_length=255,null=True)
#     image = models.FileField(upload_to='imagecategorie',null=True)
#     image_nom = models.CharField(max_length=255,null=True)
#     image_url = models.CharField(max_length=255,null=True)
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for Categorie."""

#         verbose_name = 'Categorie'
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         """Unicode representation of Categorie."""
#         return self.nom


    

# class SousCategorie(models.Model):
#     """Model definition for SousCategorie."""

#     # TODO: Define fields here
#     categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="categorie",null=True)
#     nom = models.CharField(max_length=255,null=True)
#     lien = models.URLField(max_length=255,null=True)
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for SousCategorie."""

#         verbose_name = 'SousCategorie'
#         verbose_name_plural = 'SousCategories'

#     def __str__(self):
#         """Unicode representation of SousCategorie."""
#         return self.nom


# class SousCategorieItem(models.Model):
#     """Model definition for SousCategorieItem."""

#     # TODO: Define fields here
#     categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE, related_name="souscategorie",null=True)
#     nom = models.CharField(max_length=255,null=True)
#     lien = models.URLField(max_length=255,null=True)
    
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for SousCategorieItem."""

#         verbose_name = 'SousCategorieItem'
#         verbose_name_plural = 'SousCategorieItems'

#     def __str__(self):
#         """Unicode representation of SousCategorieItem."""
#         return self.nom

# class Produit(models.Model):
#     """Model definition for Produit."""

#     # TODO: Define fields here
#     sous_categorie_item = models.ForeignKey(SousCategorieItem, on_delete=models.CASCADE, related_name="souscategorieitem",null=True,blank=True)
#     nom = models.CharField(max_length=255,null=True)
#     lien = models.URLField(max_length=255,null=True)
#     prix = models.CharField(max_length=255,null=True)
#     prix_reduit = models.CharField(max_length=255,null=True)
#     nom_marque = models.CharField(max_length=255,null=True)
#     description = models.TextField(null=True)
#     couleur = JSONField(null=True)
#     taille = ArrayField(
#         models.CharField(max_length=255),
#     )
#     en_stock = models.CharField(max_length=255,null=True)
#     note = models.CharField(max_length=255,null=True)
#     en_promotion = models.CharField(max_length=255,null=True)
#     premium = models.CharField(max_length=255,null=True)
#     nouveaute = models.CharField(max_length=255,null=True)
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for Produit."""

#         verbose_name = 'Produit'
#         verbose_name_plural = 'Produits'

#     def __str__(self):
#         """Unicode representation of Produit."""
#         return self.nom



# class Collection(models.Model):
#     """Model definition for Collection."""

#     # TODO: Define fields here
#     titre = models.CharField(max_length=255,null=True)
#     nom_auteur = models.CharField(max_length=255,null=True)
#     couleur_article = ArrayField(
#         models.CharField(max_length=255),
#         null=True
#         )
#     lien = models.URLField(max_length=255,null=True)
#     article = models.ManyToManyField(Produit, related_name='articlecollection')
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for Collection."""

#         verbose_name = 'Collection'
#         verbose_name_plural = 'Collections'

#     def __str__(self):
#         """Unicode representation of Collection."""
#         return self.titre



# class Look(models.Model):
#     """Model definition for Look."""

#     # TODO: Define fields here
#     nom_auteur = models.CharField(max_length=255,null=True)
#     image_auteur = models.FileField(upload_to='imageauteur')
#     article = models.ManyToManyField(Produit, related_name='articlelook')
#     familly = models.ManyToManyField('Look', related_name='famillylook')
#     liens_familly = ArrayField(
#         models.CharField(max_length=255),
#         null=True
#     )

#     class Meta:
#         """Meta definition for Look."""

#         verbose_name = 'Look'
#         verbose_name_plural = 'Looks'

#     def __str__(self):
#         """Unicode representation of Look."""
#         return self.nom_auteur


# class ImageProduit(models.Model):
#     """Model definition for ImageProduit."""

#     # TODO: Define fields here
#     produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="produitimage",null=True)
#     image = models.FileField(upload_to='imageproduit',null=True)
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for ImageProduit."""

#         verbose_name = 'ImageProduit'
#         verbose_name_plural = 'ImageProduits'

#     def __str__(self):
#         """Unicode representation of ImageProduit."""
#         return self.produit
    
# class ImageCollection(models.Model):
#     """Model definition for ImageCollection."""

#     # TODO: Define fields here
#     collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="collectionimage",null=True)
#     image = models.FileField(upload_to='imagecollection',null=True)
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for ImageCollection."""

#         verbose_name = 'ImageCollection'
#         verbose_name_plural = 'ImageCollections'

#     def __str__(self):
#         """Unicode representation of ImageCollection."""
#         return self.collection

# class ImageLook(models.Model):
#     """Model definition for ImageLook."""

#     # TODO: Define fields here
#     look = models.ForeignKey(Look, on_delete=models.CASCADE, related_name="lookimage",null=True)
#     image = models.FileField(upload_to='imagelook',null=True)
    
#     statut = models.BooleanField(default=False,null=True)
#     date_add = models.DateTimeField(auto_now_add=True,null=True)
#     date_upd = models.DateTimeField(auto_now=True,null=True)

#     class Meta:
#         """Meta definition for ImageLook."""

#         verbose_name = 'ImageLook'
#         verbose_name_plural = 'ImageLooks'

#     def __str__(self):
#         """Unicode representation of ImageLook."""
#         return self.look


