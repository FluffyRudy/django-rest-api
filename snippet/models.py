from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES = sorted([(style, style) for style in get_all_styles()])


class Snippet(models.Model):
    title = models.CharField(max_length=50, blank=True, default="")
    linenos = models.BooleanField(default=False)
    code = models.TextField()
    language = models.CharField(choices=LANGUAGES, default="python", max_length=50)
    style = models.CharField(choices=STYLES, default="monokai", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["updated_at"]
