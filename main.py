import yaml

class Phrases:
    positive=dict(en="Positions in favour include: ",
                  nl="Positieve standpunten zijn bijvoorbeeld:")


def generate_md(cb, lang='en'):
    def x(item):
        if item is None:
            return "-"
        if isinstance(item, str):
            return item
        return item.get(lang, item.get('en'))
    for topic, d in i.items():
        description = x(d.get('description'))
        yield f"## {topic}: {description}"
        if 'positive' in d:
            yield x(Phrases.positive) + x(d["positive"])
        if 'examples' in d:
            examples = "\n".join(f"+ {x(ex)}" for ex in d['examples'])
            yield f"#### Examples:\n {examples}"

i = yaml.safe_load(open("topics.yml"))
for lang in ['en', 'nl']:
    md = "\n\n".join(generate_md(i))
    open(f"topics-{lang}.md", "w").write(md)
