import requests
import re
cookieStr=r"BAIDUID=D61F2C9132FE6EA88EB700F4237B5648:FG=1; PSTM=1585326918; BIDUPSID=C8816D22C3FAA1C34B4B466D6B9A0A59; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; H_PS_PSSID=1458_21119_30826_30823_26350_30717; PANWEB=1; cflag=13%3A3; BDUSS=xUa2p3MkIyTGYzMVFGZlFuSEI4RWNnNlF2OGIxZ3RFbVNXNkFnMnVNRGRYcTFlRUFBQUFBJCQAAAAAAAAAAAEAAABmVMx2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN3RhV7d0YVedU; STOKEN=6f61c1dc37b6e2d57c905d0107769ca2afad559fb77a5f721daac123a0bd01ce; SCRC=3db4249eba4726cde6450bc7354eb1e3; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1585828057,1585828323; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1585828343; PANPSC=4350031624500891857%3AKkwrx6t0uHC8iVtOumXSTky7txDAjOFZ3qZ5gZSyz8auxuLtaQVK%2F0ci2O0YbEjpkLK8H6PONSRD0P1uaJ3v6KKK%2FFH5WUxXs3ltqdL44oKtBnAHN3pOonZNBoZ8i0CTW8pfgMw2m%2FrQ8rlESRQE3CZTnz2RR6t%2BZFCUk453j8DrbkBUnMiFfw%3D%3D"
urlStr=r"https://pan.baidu.com/api/list?dir=%2F&bdstoken=6969f8fe3431520b8118796eb2f2347c&logid=MTU4NTgyODM1MTExMjAuNDYzOTI3ODE2Mzk2NDg4MTc=&num=100&order=time&desc=1&clienttype=0&showempty=0&web=1&page=1&channel=chunlei&web=1&app_id=250528"
def str2CookieDir(cstr):
    regexstr=r"(\S*)=(\S*);*"
    regex=re.compile(regexstr,re.M)
    matches=regex.findall(cstr)
    cookies={}
    for match in matches:
        if(len(match)!=2):
            print("error")
            pass
        cookies.update({match[0]:match[1]})
    return cookies

def GetWebJsonContent(cookies,url):
    data=requests.get(url,cookies=cookies).text
    return data
if(__name__=="__main__"):
    print(GetWebJsonContent(str2CookieDir(cookieStr),urlStr))