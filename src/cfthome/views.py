import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from pagevisits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
  return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
  qs = PageVisit.objects.all()
  page_qs = PageVisit.objects.filter(path=request.path)
  try:
    percent = round((page_qs.count() / qs.count()) * 100, 1)
  except:
    percent = 0
  my_title = 'My Page'
  html_template = 'home.html'
  my_context = {
    'page_title': my_title,
    'page_visit_count': page_qs.count(),
    'percent': percent, 
    'total_visits_count': qs.count(),
  }
  PageVisit.objects.create(path=request.path)
  return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
  my_title = 'My Page'
  my_context = {
    'page_title': my_title,
  }

  html_ = '''
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <title>{page_title}</title>
  </head>
  <body>
    <h1>Hello {page_title}</h1>
    <p>This is a simple HTML page.</p>
  </body>
  </html>
  '''.format(**my_context)

  # html_file_path = this_dir / 'home.html'
  # html_ = html_file_path.read_text()

  return HttpResponse(html_)
