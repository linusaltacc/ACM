import re
def get_urls(body):
    body = body.replace('.png','').replace('.jpg','').replace('.jpeg','')
    try: 
        # url = str(re.search(r"""(?i)\b((?:[\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))))+(?:(([^\s()<>]+|(([^\s()<>]+))))|[^\s`!()\[\]{};:'".,<>?«»""‘’]))""", body).group())
        url = re.findall(r'(?:http://)?\w+\.\S*[^.\s]', body)
        return url
    except:
        url = ''
        return url


