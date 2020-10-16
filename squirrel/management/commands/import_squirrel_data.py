from django.core.management.base import BaseCommand, CommandError

from squirrel.models import Squirrel

import csv

from datetime import datetime

class Command(BaseCommand):
    help = 'import the squirrel data from csv'

    def add_arguments(self,parser):
        parser.add_argument('squirrel.file', help='file containing squirrel sighting details')

    def handle(self, *args, **options):
        file_=options['squirrel.file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                squ = Squirrel()
                squ.latitude = item['X']
                squ.longitude = item['Y']
                squ.unique_id = item['Unique Squirrel ID']
                squ.shift = item['Shift']
                squ.date = datetime.strptime( item['Date'], '%m%d%Y').date()
                squ.age = item['Age']
                

                squ.save()
            msg = f'you are importing from {file_}'
            self.stdout.write(self.style.SUCCESS(msg))

