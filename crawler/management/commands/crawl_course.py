from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from crawler.crawler import initial_db

class Command(BaseCommand):
    args = ''
    help = 'Help crawl the course data from NTHU.'

    def handle(self, *args, **kwargs):
        if len(args) != 2:
            print 'Please provide valid ACIXSTORE and auth_num from'
            print 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'
        initial_db(args[0], args[1])
