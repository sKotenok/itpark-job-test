from django.core.management.base import BaseCommand, CommandError
from my_app.models import Product


class Command(BaseCommand):
    help = 'Show all products stored in DB'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        ps3 = Product.objects.all().values('category__name', 'name', 'price')

        for p in ps3:
            print(p['name'], p['category__name'], p['price'])
