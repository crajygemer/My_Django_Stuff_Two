#!/usr/bin/env python

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake Pop Script
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# call Topic Model
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

# call rest of Models
def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # add fake data for each entry
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        # fake entry for webpage model
        webpg = Webpage.objects.get_or_create(
            topic=top, url=fake_url, name=fake_name)[0]

        # fake entry for access record
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Run Fake Script')
    populate(20)
    print('Run Successfully.')
