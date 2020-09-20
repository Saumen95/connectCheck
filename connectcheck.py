try:
    import httplib
except:
    import http.client as httplib

def checkInternetHttplib(url=input(), timeout=3):
    conn = httplib.HTTPConnection(url, timeout=timeout)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False