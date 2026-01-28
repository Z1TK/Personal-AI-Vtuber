from backend.service.browser import WebWork

sites = {
    "google": "https://www.google.com",
    "edge": "https://www.bing.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "reddit": "https://www.reddit.com",
    "x": "https://x.com/home",
    "instagram": "https://www.instagram.com",
}


def open_brouser(command: str) -> bool:
    search_engine = command.split().lower()
    if len(search_engine) == 2:
        url = f"https://{search_engine[1]}.com"
        WebWork.open_any_browser(url)

    if command in sites:
        WebWork.open_any_browser(command)

    return True


def request_to_youtube(command: str) -> bool:
    query = command.split()[2:]
    WebWork.search_youtube(sites["youtube"], "+".join(query))
    return True
