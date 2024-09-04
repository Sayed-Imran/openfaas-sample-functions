from jinja2 import Template

def handle(req):
    t = Template("Hello {{name}}")
    res = t.render(name="Imran")
    return res