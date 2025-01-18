from django.db import models
from django.core.validators import RegexValidator


class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        verbose_name='Описание языка', 
        help_text='Краткое описание языка программирования',
        default='Описание языка программирования временно недоступно.'
    )
    code_example = models.TextField(
        verbose_name='Пример кода', 
        help_text='Демонстрационный пример кода на языке',
        blank=True,
        null=True,
        default='# Пример кода временно недоступен'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'


class Manual(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.language.name})"


class Topic(models.Model):
    name = models.CharField(max_length=255)
    manual = models.ForeignKey(Manual, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.manual.name}"


class Tutorial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.topic.name})"


class ColorScheme(models.Model):
    language = models.OneToOneField(
        Language, 
        on_delete=models.CASCADE, 
        related_name='color_scheme'
    )
    
    # Валидатор для HEX-цветов
    hex_color_validator = RegexValidator(
        r'^#(?:[0-9a-fA-F]{3}){1,2}$', 
        'Введите корректный HEX-цвет'
    )
    
    primary_color = models.CharField(
        max_length=7, 
        validators=[hex_color_validator],
        default='#3776AB'
    )
    secondary_color = models.CharField(
        max_length=7, 
        validators=[hex_color_validator],
        default='#4B8BBE'
    )
    background_color = models.CharField(
        max_length=7, 
        validators=[hex_color_validator],
        default='#F0F4F8'
    )
    text_color = models.CharField(
        max_length=7, 
        validators=[hex_color_validator],
        default='#333333'
    )
    accent_color = models.CharField(
        max_length=7, 
        validators=[hex_color_validator],
        default='#FFD43B'
    )
    
    def __str__(self):
        return f"Color Scheme for {self.language.name}"
    
    class Meta:
        verbose_name = "Цветовая схема"
        verbose_name_plural = "Цветовые схемы"
