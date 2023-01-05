from django.db import models

# Create your models here.
class HeadParallo(models.Model):
    name = models.CharField('HeadParallo name', max_length = 30)
    name1 = models.CharField('HeadParallo name1', max_length = 30)
    name2 = models.CharField('HeadParallo name2', max_length = 30)
    name3 = models.CharField('HeadParallo name3', max_length = 30)
    name4 = models.CharField('HeadParallo name4', max_length = 30)
    name5 = models.CharField('HeadParallo name5', max_length = 30)
    about = models.TextField('HeadParallo about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HeadParallo'
        verbose_name_plural = 'HeadParallos'



class MobileArt(models.Model):
    name = models.CharField('MobileArt name', max_length=50, null=True)
    name1 = models.CharField('MobileArt name1', max_length=50, null=True)
    about = models.TextField('MobileArt about')
    about1 = models.TextField('MobileArt about1', null=True)
    img = models.ImageField('MobileArt image', upload_to='media')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'MobileArt'
        verbose_name_plural = 'MobileArts'



class HomeBody(models.Model):
    name = models.CharField('HomeBody name', max_length=50)
    about = models.TextField('HomeBody about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeBody'
        verbose_name_plural = 'HomeBodies'



class HomeFoot(models.Model):
    name = models.CharField('HomeFoot name', max_length=50)
    about = models.TextField('HomeFoot about')
    about1 = models.TextField('HomeFoot about1')
    img = models.ImageField('HomeFoot image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeFoot'
        verbose_name_plural = 'HomeFoots'



class FootHomeFoot(models.Model):
    about = models.TextField('FootHomeFoot about')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'FootHomeFoot'
        verbose_name_plural = 'FootHomeFoots'



class HomeImage(models.Model):
    img = models.ImageField('HomeImage image', upload_to='media')

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = 'HomeImage'
        verbose_name_plural = 'HomeImages'


class AboutParallo(models.Model):
    name = models.CharField('HeadParallo name', max_length = 30)
    name1 = models.CharField('HeadParallo name1', max_length = 30)
    name2 = models.CharField('HeadParallo name2', max_length = 30)
    name3 = models.CharField('HeadParallo name3', max_length = 30)
    name4 = models.CharField('HeadParallo name4', max_length = 30)
    name5 = models.CharField('HeadParallo name5', max_length = 30)
    about = models.TextField('HeadParallo about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutParallo'
        verbose_name_plural = 'AboutParallos'



class AboutAbout(models.Model):
    name = models.CharField('AboutAbout name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutAbout'
        verbose_name_plural = 'AboutAbouts'



class AboutQuality(models.Model):
    name = models.CharField('AboutQuality name', max_length=30)
    about = models.TextField('AboutQuality about')
    about1 = models.TextField('AboutQuality about1', blank=True)
    number = models.IntegerField('AboutQuality number', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutQuality'
        verbose_name_plural = 'AboutQualities'



class AboutFeature(models.Model):
    name = models.CharField('AboutFeature name', max_length=50)
    about = models.TextField('AboutFeature about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutFeature'
        verbose_name_plural = 'AboutFeatures'



class AboutFoot(models.Model):
    name = models.CharField('AboutFoot name', max_length=50)
    about = models.TextField('AboutFoot about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutFoot'
        verbose_name_plural = 'AboutFoots'



class AboutImage(models.Model):
    img = models.ImageField('AboutImage image', upload_to='media')

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = 'AboutImage'
        verbose_name_plural = 'AboutImages'



class ServicesParallo(models.Model):
    name = models.CharField('HeadParallo name', max_length = 30)
    name1 = models.CharField('HeadParallo name1', max_length = 30)
    name2 = models.CharField('HeadParallo name2', max_length = 30)
    name3 = models.CharField('HeadParallo name3', max_length = 30)
    name4 = models.CharField('HeadParallo name4', max_length = 30)
    name5 = models.CharField('HeadParallo name5', max_length = 30)
    about = models.TextField('HeadParallo about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ServicesParallo'
        verbose_name_plural = 'ServicesParallos'



class ServicesImage(models.Model):
    img = models.ImageField('ServicesImage image', upload_to='media')

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = 'ServicesImage'
        verbose_name_plural = 'ServicesImages'



class OurServices(models.Model):
    name = models.CharField('OurServices name', max_length=50)
    about = models.TextField('OurServices about')
    img = models.ImageField('OurServices image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OurServices'
        verbose_name_plural = 'OurServiceses'



class ServicesBody(models.Model):
    about = models.TextField('ServicesBody about')
    about1 = models.TextField('ServicesBody about1')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'ServicesBody'
        verbose_name_plural = 'ServicesBodies'



class ServicesFoot(models.Model):
    name = models.CharField('ServicesFoot name', max_length=50, null=True)
    name1 = models.CharField('ServicesFoot name1', max_length=50, null=True)
    name2 = models.CharField('ServicesFoot name2', max_length=50, null=True)
    name3 = models.CharField('ServicesFoot name3', max_length=50, null=True)
    name4 = models.CharField('ServicesFoot name4', max_length=50, null=True)
    name5 = models.CharField('ServicesFoot name5', max_length=50, null=True)
    about = models.TextField('ServicesFoot about', null=True)
    about1 = models.TextField('ServicesFoot about1', null=True)
    about2 = models.TextField('ServicesFoot about2', null=True)
    about3 = models.TextField('ServicesFoot about3', null=True)
    about4 = models.TextField('ServicesFoot about4', null=True)
    about5 = models.TextField('ServicesFoot about5', null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ServicesFoot'
        verbose_name_plural = 'ServicesFoots'



class TestimonialsParallo(models.Model):
    name = models.CharField('TestimonialsParallo name', max_length=30)
    name1 = models.CharField('TestimonialsParallo name1', max_length=30)
    name2 = models.CharField('TestimonialsParallo name2', max_length=30)
    name3 = models.CharField('TestimonialsParallo name3', max_length=30)
    name4 = models.CharField('TestimonialsParallo name4', max_length=30)
    name5 = models.CharField('TestimonialsParallo name5', max_length=30)
    about = models.TextField('TestimonialsParallo about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TestimonialParallo'
        verbose_name_plural = 'TestimonialParallos'



class TestimonialsImage(models.Model):
    img = models.ImageField('TestimonialsImage image', upload_to='media')

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = 'TestimonialsImage'
        verbose_name_plural = 'TestimonialsImages'



class Testimonials(models.Model):
    name = models.CharField('Testimonials name', max_length=30)
    about = models.TextField('Testimonials about')
    img = models.ImageField('Testimonials image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonialses'



class TestimonialsBody(models.Model):
    name = models.CharField('TestimonialsBody name', max_length=30)
    # name1 = models.CharField('TestimonialsBody name1', max_length=30, null=True)
    # name2 = models.CharField('TestimonialsBody name2', max_length=30, null=True)
    about = models.TextField('TestimonialsBody about')
    # about1 = models.TextField('TestimonialsBody about1', null=True)
    # about2 = models.TextField('TestimonialsBody about2', null=True)
    img = models.ImageField('TestimonialsBody image', upload_to='media')
    # img1 = models.ImageField('TestimonialsBody image1', upload_to='media', null=True)
    # img2 = models.ImageField('TestimonialsBody image2', upload_to='media', null=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TestimonialsBody'
        verbose_name_plural = 'TestimonialsBodies'



class TestimonialsFoot(models.Model):
    name = models.CharField('TestimonialsFoot name', max_length=50)
    about = models.TextField('TestimonialsFoot about')
    about1 = models.TextField('TestimonialsFoot about1')
    img = models.ImageField('TestimonialsFoot image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TestimonialsFoot'
        verbose_name_plural = 'TestimonialsFoots'



class ContactParallo(models.Model):
    name = models.CharField('ContactParallo name', max_length=30)
    name1 = models.CharField('ContactParallo name1', max_length=30)
    name2 = models.CharField('ContactParallo name2', max_length=30)
    name3 = models.CharField('ContactParallo name3', max_length=30)
    name4 = models.CharField('ContactParallo name4', max_length=30)
    name5 = models.CharField('ContactParallo name5', max_length=30)
    about = models.TextField('ContactParallo about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactParallo'
        verbose_name_plural = 'ContactParallos'



class ContactImage(models.Model):
    img = models.ImageField('ContactImage image', upload_to='media')

    def __str__(self):
        return str(self.img)

    class Meta:
        verbose_name = 'ContactImage'
        verbose_name_plural = 'ContactImages'



class Contact(models.Model):
    name = models.CharField('Contact name', max_length=30)
    about = models.TextField('Contact about')
    img = models.ImageField('Contact image', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'



class ContactBody(models.Model):
    about = models.TextField('ContactBody about')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'ContactBody'
        verbose_name_plural = 'ContactBodies'



class ContactBodi(models.Model):
    name = models.CharField('ContactBodi name', max_length=50)
    about = models.TextField('ContactBodi about')
    about1 = models.TextField('ContactBodi about1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactBodi'
        verbose_name_plural = 'ContactBodis'



class ContactFoot(models.Model):
    name = models.CharField('ContactFoot name', max_length=50)
    about = models.TextField('ContactFoot about')
    about1 = models.TextField('ContactFoot about1')
    img = models.ImageField('ContactFoot image', upload_to='media', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactFoot'
        verbose_name_plural = 'ContactFoot'



