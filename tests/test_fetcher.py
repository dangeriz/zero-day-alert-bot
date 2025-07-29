from fetcher import fetch_articles

def test_fetch_articles_returns_list():
    articles = fetch_articles()
    assert isinstance(articles, list)