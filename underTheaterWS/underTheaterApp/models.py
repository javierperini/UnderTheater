# vim: set fileencoding=utf-8 :
from __future__ import unicode_literals
from django.db import models
from address.models import AddressField
from users import Actor


class Contact(models.Model):
    number_phone = models.IntegerField(verbose_name=u'Numero de telefono')
    facebook = models.CharField(max_length=128, blank=True,
                                verbose_name=u'usuario en Facebook')
    address = AddressField()
    share_address = models.BooleanField(default=True,
                                        verbose_name=u"Compartir direccion",
                                        blank=False, null=False,
                                        help_text=u"Compartir la direccion")

    def __str__(self):
        return u"%s" % self.pk


class Theater(models.Model):
    name = models.CharField(max_length=200, unique=True)
    review = models.TextField(max_length=500,
                              verbose_name=u"reseña del teatro")
    contact = models.OneToOneField(Contact, verbose_name=u'contacto',
                                   related_name=u'theater_contact',
                                   primary_key=True)

    def __str__(self):
        return self.name


class TheaterRoom(models.Model):
    theater = models.ForeignKey(Theater, verbose_name=u'room',
                                related_name=u'theater_room')
    capacity = models.IntegerField(verbose_name=u'cantidad de asientos libres')
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return self.room_name


class PlayTheater(models.Model):
    play_name = models.CharField(max_length=200)
    synopsis = models.TextField(max_length=500,
                                verbose_name="Sinopsis de la obra")
    theater = models.ManyToManyField(Theater, verbose_name=u'play',
                                     related_name=u'theater')
    room_theater = models.ManyToManyField(TheaterRoom,
                                          verbose_name=u'sala de la obra',
                                          related_name='room')
    actors = models.ManyToManyField(Actor, verbose_name=u'categorías')
    picture = models.ImageField(upload_to="playImages")

    def __str__(self):
        return self.play_name


class PlayPrice(models.Model):
    play = models.ForeignKey(PlayTheater, verbose_name=u'PlayPrice',
                             related_name=u'play_price')
    price_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.prince_name


class DateShow(models.Model):
    play = models.ForeignKey(PlayTheater, verbose_name=u'date show',
                             related_name=u'play_date_show')
    date_show = models.DateTimeField(auto_now=True,
                                     verbose_name=u'dia y horario del show')

    def __str__(self):
        return self.date_show.strftime("%y-%m-%d %H:%M")
