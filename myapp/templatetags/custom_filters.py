# myapp/templatetags/custom_filters.py
import datetime
from django import template

register = template.Library()

@register.filter
def time_since(value):
    if not value:
        return ""
    now = datetime.datetime.now(datetime.timezone.utc)
    diff = now - value
    if diff.days == 0:
        if diff.seconds < 60:
            return "Just now"
        if diff.seconds < 3600:
            return f"{diff.seconds // 60} minutes ago"
        return f"{diff.seconds // 3600} hours ago"
    if diff.days == 1:
        return "Yesterday"
    if diff.days < 30:
        return f"{diff.days} days ago"
    return value.strftime("%Y-%m-%d")
