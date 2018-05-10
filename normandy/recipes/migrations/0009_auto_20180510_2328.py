# Generated by Django 2.0.5 on 2018-05-10 23:28

from django.db import migrations


def enabled_to_enabled_state(apps, schema_editor):
    Recipe = apps.get_model('recipes', 'Recipe')
    EnabledState = apps.get_model('recipes', 'EnabledState')

    for recipe in Recipe.objects.filter(enabled=True):
        if recipe.approved_revision:
            EnabledState.objects.create(revision=recipe.approved_revision, enabled=True)


def enabled_state_to_enabled(apps, schema_editor):
    Recipe = apps.get_model('recipes', 'Recipe')

    for recipe in Recipe.objects.exclude(approved_revision=None):
        enabled_state = recipe.approved_revisison.enabled_states.first()
        if enabled_state and enabled_state.enabled():
            recipe.enabled = True
            recipe.save()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20180510_2252'),
    ]

    operations = [
        migrations.RunPython(enabled_to_enabled_state, enabled_state_to_enabled)
    ]
