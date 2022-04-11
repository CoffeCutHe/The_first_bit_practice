 r = requests.post(url,
                  data=text.encode('utf-8'),
                  headers={'Content-type': 'text/plain; charset=utf-8'})
print(r.json())