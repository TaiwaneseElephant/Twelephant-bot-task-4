import pywikibot as pwb
import time
def main(times):
  Site = pwb.Site("zh", "wikipedia")
  t = 0
  for page in site.search(r'insource:/id\s*=\s*\"spoiler\"\s*style\s*=/', namespaces=(1, 4, 5), content=True):
    page.text = page.text.replace('id="spoiler" style="', \
          'style="border-top: 2px solid var(--border-color-base, #a2a9b1); border-bottom: 2px solid var(--border-color-base, #a2a9b1); ')
    page.save(summary="清理#spoiler", minor=true, bot=true)
    t += 1
    if t >= times:
      return
    time.sleep(5)
main()
