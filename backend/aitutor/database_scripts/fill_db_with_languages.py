import os
import sys
import json
import django
from django.db import transaction

# Add project path
sys.path.append('/home/nadgox/Public/PublicProjects/Python/AI-Tutorial/backend/aitutor')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aitutor.settings')

# Initialize Django
django.setup()

from tutorials.models import Language, ColorScheme

def fill_languages_and_color_schemes():
    # Load languages from JSON file
    json_path = os.path.join(
        '/home/nadgox/Public/PublicProjects/Python/AI-Tutorial/backend/aitutor/database_scripts', 
        'languages.json'
    )
    
    with open(json_path, 'r', encoding='utf-8') as f:
        languages_data = json.load(f)
    
    # Use transaction to ensure data integrity
    with transaction.atomic():
        # Clear existing languages and color schemes
        ColorScheme.objects.all().delete()
        Language.objects.all().delete()
        
        for lang_data in languages_data:
            # Create language
            language = Language.objects.create(
                name=lang_data['name'],
                description=lang_data['description'],
                code_example=lang_data['code_example']
            )
            
            # Create color scheme
            color_scheme_data = lang_data['color_scheme']
            ColorScheme.objects.create(
                language=language,
                primary_color=color_scheme_data['primary_color'],
                secondary_color=color_scheme_data['secondary_color'],
                background_color=color_scheme_data['background_color'],
                text_color=color_scheme_data['text_color'],
                accent_color=color_scheme_data['accent_color']
            )
            
            print(f"Added language: {language.name}")

def main():
    fill_languages_and_color_schemes()

if __name__ == '__main__':
    main()