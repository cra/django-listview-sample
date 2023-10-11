from django.core.management.base import BaseCommand
from myapp.models import MyModel

class Command(BaseCommand):
    help = 'Create some initial objects for MyModel'

    def handle(self, *args, **kwargs):
        names = ['Object 1', 'Object 2', 'Object 3']
        for name in names:
            MyModel.objects.create(name=name)
        self.stdout.write(self.style.SUCCESS('Successfully created objects'))

