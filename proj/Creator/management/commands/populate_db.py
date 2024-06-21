import json
import os
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from Creator.models import Creator
from Content.models import Content

class Command(BaseCommand):
    help = 'Populates the database with creators and content from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file_path']

        if not os.path.exists(json_file_path):
            raise CommandError(f'File "{json_file_path}" does not exist')

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise CommandError('Invalid JSON format: Expected a list of creators')

        with transaction.atomic():
            Creator.objects.all().delete()
            Content.objects.all().delete()

            for creator_data in data:
                creator = Creator.objects.create(
                    name=creator_data['name'],
                    username=creator_data['username'],
                    rating=creator_data['rating'],
                    platform=creator_data['platform']
                )

                Content.objects.create(
                    creator=creator,
                    url=creator_data['content']
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
