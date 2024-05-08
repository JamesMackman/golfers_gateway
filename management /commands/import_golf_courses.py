import csv
import requests
from django.core.management.base import BaseCommand
from golf_courses.models import GolfClub 


class Command(BaseCommand):
    help = 'Import golf courses from CSV file'

    def handle(self, *args, **options):
        csv_url = 'https://storage.cloud.google.com/golfcourses/Bucket%20List%20Golf%20-%20Sheet1.csv'

        try:
            response = requests.get(csv_url)
            response.raise_for_status()  # Raise exception for HTTP errors
            csv_data = response.text.splitlines()
            csv_reader = csv.reader(csv_data)

            for row in csv_reader:
                # Extract name and cost from each row
                name, cost = row[0], row[1] 

                # Create or update GolfClub objects based on CSV data
                golf_club, created = GolfClub.objects.update_or_create(
                    name=name,
                    defaults={
                        'price': cost  
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created golf club: {golf_club.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated golf club: {golf_club.name}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to import golf clubs: {str(e)}'))
