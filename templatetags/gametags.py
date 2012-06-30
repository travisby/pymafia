from django import template

register = template.Library()

@register.filter(name='game_size')
def game_size(game):
    return game.character_set.count
