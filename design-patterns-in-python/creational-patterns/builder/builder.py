# BUILDER PATTERN
# examples taken from ArjanCodes

# The builder pattern allows you to build complex objects step by step in a clean, easy, and manageable manner
# The idea is to have separate functions that build aspects of an object rather than having a very large single initializer
# This allows us to configure our object piece by piece

# The only problem with the builder pattern is that it involves a lot of boilerplate as seen below
# THis may increase how verbose the code is and may result in you making mistakes easier


from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class HTMLPage:
    title: str
    metadata: dict[str, str]
    body_elements: list[str]

    def render(self) -> str:
        body = "\n".join(self.body_elements)
        meta_tags = "\n".join(
            f'<meta name="{name}" content="{value}">'
            for name, value in self.metadata.items()
        )
        return f"""<!DOCTYPE html>
                    <html>
                    <head>
                    <title>{self.title}</title>
                    {meta_tags}
                    </head>
                    <body>
                    {body}
                    </body>
                    </html>"""


class HTMLBuilder:
    # This is our builder class
    # Here you see functions defined that will build our HTML Page step by step

    def __init__(self) -> None:
        self._title: str = "Untitled"
        self._body: list[str] = []
        self._metadata: dict[str, str] = {}

    def set_title(self, title: str) -> Self:
        self._title = title
        return self

    def add_header(self, text: str, level: int = 1) -> Self:
        self._body.append(f"<h{level}>{text}</h{level}>")
        return self

    def add_paragraph(self, text: str) -> Self:
        self._body.append(f"<p>{text}</p>")
        return self

    def add_button(self, label: str, onclick: str = "#") -> Self:
        self._body.append(
            f"<button onclick=\"location.href='{onclick}'\">{label}</button>"
        )
        return self

    def add_metadata(self, name: str, content: str) -> Self:
        self._metadata[name] = content
        return self

    def build(self) -> HTMLPage: # This is another important aspect of the builder pattern
        return HTMLPage(self._title, self._metadata, self._body)
