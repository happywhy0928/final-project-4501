from django.core.management.base import BaseCommand, CommandError
  
from squirrel.models import Squirrel
import csv
class Command(BaseCommand):
    help = 'export the squirrel data scv'
    def add_arguments(self, parser):
        parser.add_argument('export_path', help = 'A path that your file to export')
    def handle(self, *args, **options):
        file_ = options['export_path']
        squirrels = Squirrel.objects.all()
        with open(file_, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Latitude', 'Longitude', 'Unique_ID', 'Shift', 'Date',
                             'Age', 'Primary_fur_Color', 'Running', 'Eating', 'Climbing'])
            for squirrel in squirrels:
                writer.writerow([squirrel.latitude, squirrel.longitude, squirrel.unique_id,
                                squirrel.shift, squirrel.date, squirrel.age, squirrel.furColor,
                                squirrel.running, squirrel.eating, squirrel.climbing])
        fp.close()
        print(f'data exports successfully!')
