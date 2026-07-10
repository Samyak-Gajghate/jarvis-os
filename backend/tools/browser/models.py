from pydantic import BaseModel


class PageContent(BaseModel):
    url: str
    title: str
    text: str


class BrowserMetadata(BaseModel):
    browser: str = "chromium"
    headless: bool = True