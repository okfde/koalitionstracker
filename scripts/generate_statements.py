from datetime import date
import re
import sys

import yaml


MARKDOWN_LINK = re.compile(r"\[([^\]]+)\]\(#([^\)]+)\)")


def make_statement(title, statement_id):
    return {
        "summary": title,
        "id": statement_id,
        "status": "not_implemented",
        "last_update": date.today().isoformat(),
    }


def main(filename):
    with open(filename) as f:
        content = f.read()

    markdown = content.split('---\n')[-1]
    links = MARKDOWN_LINK.findall(markdown)
    statements = [make_statement(title, link_id) for title, link_id in links]
    output = yaml.safe_dump(
        statements,
        explicit_start=False,
        explicit_end=False,
        allow_unicode=True,
        default_flow_style=False
    )
    print(output)


if __name__ == "__main__":
    main(*sys.argv[1:])
