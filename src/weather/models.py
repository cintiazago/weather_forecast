from django.db import models


class City(models.Model):
    """
    Represents the different cities with weather forecast
    """
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    population = models.IntegerField()

    def __str__(self):
        return self.name


class Forecast(models.Model):
    """
    Represents the weather forecast associated to the cities
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # temperatures saved with Unit as Kelvin
    temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()
    # pressures saved with unit as Atmospheric pressure (hPa)
    pressure = models.FloatField()
    pressure_at_sea = models.FloatField()
    pressure_at_ground = models.FloatField()
    # humidity and cloudiness as percentage
    humidity = models.FloatField()
    cloudiness = models.FloatField()
    weather_description = models.CharField(max_length=250)
    # wind speed as meter/sec
    wind_speed = models.FloatField()
    wind_degrees = models.FloatField()

    def __str__(self):
        return 'Forecast for %s on %s at %s'.format(self.city.name,
                                                    str(self.date),
                                                    str(self.time))
