import django
import django.conf
import json


if __name__ == "__main__":

    # 1: Create base Django Objects

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['.'],
        }
    ]
    django.conf.settings.configure(TEMPLATES=TEMPLATES)
    django.setup()
    ctx=dict()
    # 2 read the template
    template = django.template.loader.get_template('./templates/Template1.xml')

    # 3 read mapping values and build internal object to allow mapping
    ### Retrieves PIM content and builds an object
    with open('./templates/Template1.json', 'r') as f:
        mappings=json.load(f)

    # 4 map this
    result=template.render(mappings)
    print('Resulting rendered template')
    print(result)
    # 5 update PIM repositories with mapping actions taken and so on ...