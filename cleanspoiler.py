import pywikibot as pwb
import time
import re
def main(times):
  site = pwb.Site("zh", "wikipedia")
  t=28
  for page in site.search(r'insource:/id\s*=\s*\"spoiler\"\s*style\s*=\s*\"/', namespaces=(1, 4, 5), content=True):
    page.text = re.sub(r'id\s*=\s*"spoiler"\s*style\s*=\s*"', \
          'style="border-top: 2px solid var(--border-color-base, #a2a9b1); border-bottom: 2px solid var(--border-color-base, #a2a9b1); ', \
                     page.text)
    t += 1
    page.save(summary=("[[User:Twelephant-bot/task/4|Task 4]]：清理#spoiler，第%d筆編輯" % t), minor=True, bot=True)
    if t == times:
      break
    time.sleep(10)
main(50)
