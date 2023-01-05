from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import HeadParallo, MobileArt, HomeBody, HomeFoot, FootHomeFoot, AboutParallo, AboutAbout, AboutQuality, AboutFeature, AboutFoot, AboutImage, HomeImage, ServicesParallo, ServicesImage, OurServices, ServicesBody, ServicesFoot, TestimonialsParallo, TestimonialsImage, Testimonials, TestimonialsBody, TestimonialsFoot, ContactParallo, ContactImage, Contact, ContactBody, ContactBodi, ContactFoot

# Create your views here.

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        headparallo = HeadParallo.objects.all()
        mobileart = MobileArt.objects.all()
        homebody = HomeBody.objects.all()
        homefoot = HomeFoot.objects.all()
        foothomefoot = FootHomeFoot.objects.all()
        homeimage = HomeImage.objects.all()
        return render(request, self.template_name, {'headparallo':headparallo, 'mobileart':mobileart, 'homebody':homebody, 'homefoot':homefoot, 'foothomefoot':foothomefoot, 'homeimage':homeimage})



class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        aboutparallo = AboutParallo.objects.all()
        aboutabout = AboutAbout.objects.all()
        aboutquality = AboutQuality.objects.all()
        aboutfeature = AboutFeature.objects.all()
        aboutfoot = AboutFoot.objects.all()
        aboutimage = AboutImage.objects.all()
        return render(request, self.template_name, {'aboutparallo':aboutparallo, 'aboutabout':aboutabout, 'aboutquality':aboutquality, 'aboutfeature':aboutfeature, 'aboutfoot':aboutfoot, 'aboutimage':aboutimage})



class ServicesListView(ListView):
    template_name = 'services.html'

    def get(self, request):
        servicesparallo = ServicesParallo.objects.all()
        servicesimage = ServicesImage.objects.all()
        ourservices = OurServices.objects.all()
        servicesbody = ServicesBody.objects.all()
        servicesfoot = ServicesFoot.objects.all()
        return render(request, self.template_name, {'servicesparallo':servicesparallo, 'servicesimage':servicesimage, 'ourservices':ourservices, 'servicesbody':servicesbody, 'servicesfoot':servicesfoot})



class TestimonialsListView(ListView):
    template_name = 'testimonials.html'

    def get(self, request):
        testimonialsparallo = TestimonialsParallo.objects.all()
        testimonialsimage = TestimonialsImage.objects.all()
        testimonials = Testimonials.objects.all()
        testimonialsbody = TestimonialsBody.objects.all()
        testimonialsfoot = TestimonialsFoot.objects.all()
        return render(request, self.template_name, {'testimonialsparallo':testimonialsparallo, 'testimonialsimage':testimonialsimage, 'testimonials':testimonials, 'testimonialsbody':testimonialsbody, 'testimonialsfoot':testimonialsfoot})



class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        contactparallo = ContactParallo.objects.all()
        contactimage = ContactImage.objects.all()
        contact = Contact.objects.all()
        contactbody = ContactBody.objects.all()
        contactbodi = ContactBodi.objects.all()
        contactfoot = ContactFoot.objects.all()
        return render(request, self.template_name, {'contactparallo':contactparallo, 'contactimage':contactimage, 'contact':contact, 'contactbody':contactbody, 'contactbodi':contactbodi, 'contactfoot':contactfoot})
