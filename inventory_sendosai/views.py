import os
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
import markdown

class HomeView(View):
    def get(self, request, *args, **kwargs):
        readme_path = os.path.join(settings.BASE_DIR, 'README.md')
        with open(readme_path, 'r', encoding='utf-8') as readme_file:
            content = readme_file.read()
        html_content = markdown.markdown(content)
        context = {'content': html_content}
        return render(request, 'home.html', context)