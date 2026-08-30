import pywikibot as pwb
import time
import re
def main():
  Site = pwb.Site("zh", "wikipedia")
  for page in site.search(r'insource:/id\s*=\s*\"spoiler\"\s*style\s*=/', namespaces=(1, 4, 5), content=True):
    page.text = re.sub(r'id\s*=\s*\"spoiler\"\s*style\s*=/"', \
          'style="border-top: 2px solid var(--border-color-base, #a2a9b1); border-bottom: 2px solid var(--border-color-base, #a2a9b1); ', \
                     page.text)
    page.save(summary="[[User:Twelephant-bot/task/4|Task 4]]：清理#spoiler", minor=true, bot=true)
    time.sleep(10)
main()
