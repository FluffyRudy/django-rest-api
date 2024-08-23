import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/snippets/"

username = "apple"
password = "zeldarpg"

data = [
    {
        "title": "watermelon",
        "code": 'def hello():\n    print("watermelon")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "watermelon",
    },
    {
        "title": "xigua",
        "code": 'def hello():\n    print("xigua")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "xigua",
    },
    {
        "title": "yellow watermelon",
        "code": 'def hello():\n    print("yellow watermelon")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "yellow watermelon",
    },
    {
        "title": "zucchini",
        "code": 'def hello():\n    print("zucchini")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "zucchini",
    },
    {
        "title": "apricot",
        "code": 'def hello():\n    print("apricot")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "apricot",
    },
    {
        "title": "blackberry",
        "code": 'def hello():\n    print("blackberry")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "blackberry",
    },
    {
        "title": "cantaloupe",
        "code": 'def hello():\n    print("cantaloupe")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "cantaloupe",
    },
    {
        "title": "dragonfruit",
        "code": 'def hello():\n    print("dragonfruit")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "dragonfruit",
    },
    {
        "title": "elderflower",
        "code": 'def hello():\n    print("elderflower")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "elderflower",
    },
    {
        "title": "figs",
        "code": 'def hello():\n    print("figs")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "figs",
    },
    {
        "title": "grapefruit",
        "code": 'def hello():\n    print("grapefruit")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "grapefruit",
    },
    {
        "title": "huckleberry",
        "code": 'def hello():\n    print("huckleberry")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "huckleberry",
    },
    {
        "title": "italian plum",
        "code": 'def hello():\n    print("italian plum")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "italian plum",
    },
    {
        "title": "jackfruit",
        "code": 'def hello():\n    print("jackfruit")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "jackfruit",
    },
    {
        "title": "kumquat",
        "code": 'def hello():\n    print("kumquat")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "kumquat",
    },
    {
        "title": "lime",
        "code": 'def hello():\n    print("lime")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "lime",
    },
    {
        "title": "mangosteen",
        "code": 'def hello():\n    print("mangosteen")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "mangosteen",
    },
    {
        "title": "nectarines",
        "code": 'def hello():\n    print("nectarines")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "nectarines",
    },
    {
        "title": "olive",
        "code": 'def hello():\n    print("olive")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "olive",
    },
    {
        "title": "plum",
        "code": 'def hello():\n    print("plum")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "plum",
    },
    {
        "title": "quince",
        "code": 'def hello():\n    print("quince")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "quince",
    },
    {
        "title": "rhubarb",
        "code": 'def hello():\n    print("rhubarb")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "rhubarb",
    },
    {
        "title": "starfruit",
        "code": 'def hello():\n    print("starfruit")',
        "linenos": True,
        "language": "python",
        "style": "monokai",
        "owner": "starfruit",
    },
]


for item in data:
    response = requests.post(url, json=item, auth=HTTPBasicAuth(username, password))
    print(response.url)
    if response.status_code == 201:
        print(f"Successfully created: {item['title']}")
    else:
        print(
            f"Failed to create {item['title']}: {response.status_code} - {response.text}"
        )
