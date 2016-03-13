from django.core.management.base import BaseCommand, CommandError
from main.models import Document

class Command(BaseCommand):
    help = 'Search peoples'

    def add_arguments(self, parser):
        parser.add_argument('education', nargs='+', type=str)
    
    def handle(self, *args, **options):
	for item in options['education']:
	    try:
                doc = Document.objects.get(education=item)
	    except Document.DoesNotExist:
                raise CommandError('This document doesn`t exist')

            doc.opened = False
            doc.save()
	    peoples = doc.people.all()
	    for i in peoples:
                self.stdout.write(self.style.SUCCESS('%s'%i.name))
