import re
from django.template import Library
from django.template.defaultfilters import stringfilter
# from django.conf import settings
from django.utils.safestring import mark_safe

from vaticinator import Vaticinator

register = Library()
vaticinator = Vaticinator()


@register.simple_tag
def random_fortune(*args, **kwargs):
    # return f'args {len(args)} kw {len(kwargs)}'
    vaticinator.set_default_options()
    vaticinator.process_options(*args, **kwargs)
    return vaticinator.fortune


@register.filter(is_safe=True)
@stringfilter
def image_click(html, func):
    # return re.sub(r'<img.*src="data:image\/([a-zA-Z]*);base64,([^"]*)"s>',
    return re.sub(r'<img ([^>]*)>',
                  f'<img onclick="{func}" \\1>',
                  html)


@register.simple_tag
def font_links():
    FONTS = (
        'Shadows+Into+Light',
        'IM+Fell+English+SC',
        'Sedgwick+Ave+Display',
        'Acme',
        'Nothing+You+Could+Do',
        'VT323',
        'Black+Ops+One',
        'Dosis:wght@200;300;400;500;600;700')
    links = [
        '<link rel="preconnect" \
            href="https://fonts.googleapis.com" />',
        '<link rel="preconnect" \
            href="https://fonts.gstatic.com" crossorigin />'
    ]
    # links.append(
    #     '<link href="https://fonts.googleapis.com/css2?'
    #     + "family&".join([font for font in FONTS])
    #     + '&display=swap rel="stylesheet" />'
    # )
    for font in FONTS:
        links.append(
            f'<link href="https://fonts.googleapis.com/css2?family={font}&display=swap" rel="stylesheet" / >'
        )
    return mark_safe('\n'.join(links))
