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

            str_to_bool = lambda x : (True if x.lower() == 'true' else False)

            for item in reader:
                squ = Squirrel()
                squ.latitude = item['X']
                squ.longitude = item['Y']
                squ.unique_id = item['Unique Squirrel ID']
                squ.shift = item['Shift']
                squ.date = datetime.strptime( item['Date'], '%m%d%Y').date()
                squ.age = item['Age']
                squ.furColor = item['Primary Fur Color']
                squ.running = str_to_bool(item['Running'])
                squ.eating = str_to_bool(item['Eating'])
                squ.climbing = str_to_bool(item['Climbing'])
                id_count = Squirrel.objects.filter(unique_id = squ.unique_id).count()
                if id_count > 0:
                    continue

                squ.save()
            msg = f'you are importing from {file_}'
            self.stdout.write(self.style.SUCCESS(msg))

