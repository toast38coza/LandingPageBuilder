from django.shortcuts import render
import yaml
def page(request):

	yml_string = open('data/index.yml')
	context = yaml.load(yml_string)
	return render(request, 'app/bootstrap/themes/vanilla/base.html', context)
