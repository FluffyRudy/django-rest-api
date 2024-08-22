from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES = sorted([(style, style) for style in get_all_styles()])


class Snippet(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="snippetss", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50, blank=True, default="")
    linenos = models.BooleanField(default=False)
    code = models.TextField()
    language = models.CharField(choices=LANGUAGES, default="python", max_length=50)
    style = models.CharField(choices=STYLES, default="monokai", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        ordering = ["updated_at"]
