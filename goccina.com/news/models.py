from django.db import models
from slugify import slugify
# Create your models here.
class Menu(models.Model):
	title = models.CharField(max_length=255,verbose_name="Menu_adı",null=True,blank=True)
	url = models.CharField(max_length=255,verbose_name="Site_urli",null=True,blank=True)


	class Meta:
		ordering = ('-id',)
		verbose_name = 'Menu'
		verbose_name_plural = 'Menuler'

	def __str__(self):
		return self.title


class Slider(models.Model):
	image = models.ImageField(upload_to="slider/",verbose_name="Şekil",null=True,blank=True)
	status = models.BooleanField(default=True, verbose_name='durumu')

	class Meta:
		ordering = ('-id',)
		verbose_name = 'Kaydırıcı'
		verbose_name_plural = 'Kaydırıcılar'

	def __str__(self):
		return self.image.name[:14]




class News(models.Model):
	title = models.CharField(max_length=255, verbose_name="Başlık", null=True, blank=True)
	content = models.TextField(verbose_name="Metni", null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	background = models.ImageField(verbose_name="Arka plan resmi",upload_to='images/',null=True,blank=True)
	slug = models.CharField(max_length=255, verbose_name='Slug',null=True, blank=True)

	class Meta:
		ordering = ('-created',)
		verbose_name = 'Haber'
		verbose_name_plural = 'Haberler'
		
	def __str__(self):
		return self.title

	def save(self,*args,**kwargs):
		super(News, self).save(*args, **kwargs)
		self.slug = slugify(self.title_tr.lower())
		super(News, self).save(*args, **kwargs)

	@property
	def get_slug(self):
		return '{}{:02}'.format(self.slug, self.id)
		


class Teams(models.Model):
	name = models.CharField(max_length=255,null=True,blank=True,verbose_name='adı')
	email = models.CharField(max_length=255,null=True,blank=True,verbose_name='email')
	text = models.TextField(null=True,blank=True,verbose_name='alıntı')
	image = models.ImageField(upload_to='teams/',null=True,blank=True)

	class Meta:
		ordering = ('-id',)
		verbose_name = 'Takim'
		verbose_name_plural = 'Takimlar'

	def __str__(self):
		return self.name


class Category(models.Model):
	text = models.CharField(max_length=255,verbose_name="Adi")
	url = models.CharField(max_length=255, verbose_name="Url",null=True,blank=True)

	
	def get_url_category(self):
		return '/reference/' + self.text_en.replace(' ','-')


	def save(self, *args,**kwargs):
		self.url = Category.get_url_category(self)
		super(Category,self).save(*args, **kwargs)



	class Meta:
		ordering = ('-id',)
		verbose_name = 'Kategori'
		verbose_name_plural = "Kategoriler"

	def __str__(self):
		return self.text



class Reference(models.Model):
	text = models.CharField(max_length=255,null=True,blank=True,verbose_name="Başlık")
	image = models.ImageField(upload_to='reference/',null=True,blank=True, verbose_name="Şekli")

	class Meta:
		ordering = ('-id',)
		verbose_name = 'Referans'
		verbose_name_plural = 'Referanslarimiz'

	def __str__(self):
		return self.title


class Collection(models.Model):
	text = models.CharField(max_length=255,null=True,blank=True, verbose_name="Başlık")
	image = models.ImageField(upload_to='collection/',null=True,blank=True, verbose_name="Şekli")
	types = models.ForeignKey(Category, null=True,blank=True, verbose_name="Tipi")

	class Meta:
		ordering = ('-id',)
		verbose_name = 'Koleksiyon'
		verbose_name_plural = 'Koleksiyonlar'

	def __str__(self):
		return self.text

	@property
	def get_url(self):
		return self.text_en



class NewsImage(models.Model):
    news_fk = models.ForeignKey(News, related_name='images')
    image = models.ImageField(upload_to='images/', null=True,blank=True)




class Contact(models.Model):
	address = models.CharField(max_length=255,null=True,blank=True,verbose_name='adresi')
	number = models.CharField(max_length=200,null=True,blank=True,verbose_name='numara')
	email = models.EmailField(null=True,blank=True,verbose_name='email')
	facebook = models.URLField(verbose_name="Facebook",null=True,blank=True)
	twitter = models.URLField(verbose_name="Twitter",null=True,blank=True)
	google = models.URLField(verbose_name="Google+",null=True,blank=True)
	instagram = models.URLField(verbose_name="Instagram",null=True,blank=True)

	class Meta:
		verbose_name = 'İletişim'
		verbose_name_plural = 'kontaklar'
		ordering = ('-id',)


	def __str__(self):
		return self.address



