from bs4 import BeautifulSoup


class ContentExtractor:
    """Extract readable text from HTML."""

    def extract(
        self,
        html: str,
    ) -> tuple[str, str]:

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        for tag in soup(
            [
                "script",
                "style",
                "noscript",
                "svg",
                "iframe",
            ]
        ):
            tag.decompose()

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "Untitled"
        )

        text = soup.get_text(
            separator=" ",
            strip=True,
        )

        return title, text