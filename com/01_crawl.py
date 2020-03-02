from libs.crawler import crawl

url = "https://www.instagram.com/explore/tags/%EB%8B%AC%EA%B3%A0%EB%82%98%EC%BB%A4%ED%94%BC/"

pageString = crawl(url)
print(pageString)
