# Generated by Django 2.2 on 2020-01-14 23:32

import apps.base.wagtail.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('articles', '0003_articlepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('markdown', apps.base.wagtail.blocks.MarkDownBlock())], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
