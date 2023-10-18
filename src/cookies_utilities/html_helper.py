from typing import List, Optional, Callable


class CssHelper(dict):
    def __init__(self) -> None:
        super().__init__({
            'body': {
                'margin': '20px', 'color': '#303030',
                'font-size': '88%', 'letter-spacing': '0.035em',
                'font-family': '\'Trebuchet MS\', sans-serif',
            },
            'table': {'border-collapse': 'collapse'},
            'th': {'padding-right': '1.0em'},
            'td': {'padding-right': '1.0em', 'border-top': '1px solid darkgray'},
            'pre': {
                'background': '#f3f3f3', 'border': '1px solid darkgray',
                'padding': '1em', 'margin': '1em 0', 'overflow': 'auto',
                'white-space': 'pre', 'word-wrap': 'normal',
            },
            'code': {'background': '#f3f3f3'},
        })

    def set(self, element: str, property: str, value: str) -> None:
        if element not in self:
            self[element] = {}
        self[element][property] = value

    def to_list(self) -> List[str]:
        li = []
        for k, v in self.items():
            s = k + ' {'
            for k_, v_ in v.items():
                s += f' {k_}: {v_};'
            s += ' }'
            li.append(s)
        return li


class HtmlHelper:
    """ Class to help with creating an HTML file.
    """
    def __init__(self, title: Optional[str] = None) -> None:
        """ 
        :param title: The title of the HTML (optional).
        """
        self.title = title
        self.meta = [
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        ]
        self.css = CssHelper()
        self.body_content = []

    def append_markdown(self, md_path: str, converter: Callable[[str], str]) -> None:
        """ Reads the markdown file, converts it to HTML, and appends to the body.

        :param md_path: Path to the markdown file.
        :param converter: Function used to convert markdown to HTML.
        """
        with open(md_path, 'r', encoding='utf-8') as ifile:
            md = ifile.read()
        markup = converter(md)
        self.body_content.append(markup)

    def append(self, s: str) -> None:
        """ 
        :param s: String to be appended to the HTML body.
        """
        self.body_content.append(s)

    def append_heading(self, level: int, s: str) -> None:
        """ 
        :param level: Integer indicating the heading level.
        :param s: Heading String.
        """
        if level not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Expected level in [1, 2, 3, 4, 5, 6]")
        self.body_content.append(f'<h{level}>{s}</h{level}>')

    def _get_content(self) -> List[str]:
        title_ = [f'<title>{self.title}</title>'] if self.title is not None else []
        return ['<!DOCTYPE html>', '<html>', '<head>'] + self.meta \
            + ['<style type="text/css"><!--'] + self.css.to_list() + ['--></style>'] \
            + title_ + ['</head>', '<body>'] + self.body_content + ['</body>', '</html>']

    def to_html(self, out_path: str) -> None:
        """ 
        :param out_path: Output path for the HTML file.
        """
        content_ = '\n'.join(self._get_content())
        with open(out_path, 'w', encoding='utf-8') as ofile:
            ofile.write(content_)
