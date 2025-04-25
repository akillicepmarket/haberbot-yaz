import feedparser
from datetime import datetime

# Haber kaynakları
sources = [
    "https://www.webrazzi.com/feed/",
    "https://shiftdelete.net/feed",
    "https://www.donanimhaber.com/rss/tum/"
]

# HTML içeriği
today_date = datetime.now().strftime("%d.%m.%Y")
html_content = f'<!-- Güncelleme Tarihi: {today_date} -->\n<ul class="haberler">\n'

for url in sources:
    feed = feedparser.parse(url)
    for entry in feed.entries[:3]:  # Her kaynaktan 3 haber alıyoruz
        title = entry.title
        link = entry.link
        summary = entry.summary if 'summary' in entry else ''
        html_content += f'  <li>\n'
        html_content += f'    <h2><a href="{link}" target="_blank" rel="noopener noreferrer">{title}</a></h2>\n'
        html_content += f'    <p>{summary}</p>\n'
        html_content += f'  </li>\n'

html_content += '</ul>'

# Dosyayı kaydet
with open('haberler.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
