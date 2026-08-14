import pywikibot as pwb
import time
def main():
  Site = pwb.Site("zh", "wikipedia")
  t = 0
  for page in site.search(r'insource:/id\s*=\s*\"spoiler\"\s*style\s*=/', namespaces=(1, 4, 5), content=True):
    page.text = page.text.replace('id="spoiler" style="', \
          'style="border-top: 2px solid var(--border-color-base, #a2a9b1); border-bottom: 2px solid var(--border-color-base, #a2a9b1); ')
    page.save(summary="（[[Wikipedia:机器人/申请/Twelephant-bot/3|BRFA]]）清理#spoiler", minor=true, bot=true)
    time.sleep(10)
main()
