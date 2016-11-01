import urllib2
import re
import os


class meiziUrl(object):
    def __init__(self, url, mainpath):
        self.url=url
        self.mainpath=mainpath
       
        if os.path.exists(mainpath):
            pass
        else:
            os.makedirs(mainpath)
    def __getHtml(self):
        url=self.url
        header={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.5"}
        res=urllib2.Request(url,headers=header)
        response=urllib2.urlopen(res)
        html=response.read()
        print html
        return html
    def __getmainUrl(self):
        html=self.__getHtml()
        ruler=' href="(http://[^\/]*/)(\d+)"'
        reg=re.compile(ruler)
        urllist=re.findall(reg,html)
        print urllist
        return urllist
    def __formatxulie(self):
        meiziurllist=self.__getmainUrl()
        mainpath=self.mainpath
        path=self.__generatemeizixulie(mainpath, meiziurllist)
        f=open(path,'r')
        path=mainpath+'format.txt'
        newf=open(path,'w')
        newf=open(path,'r')
        xulieset=set([])
        for xulie in f.readlines():
            xulieset.add(xulie)
        for xulie in newf.readlines():
            xulieset.add(xulie)
        newf=open(path,'w')
        for var in xulieset:
            newf.write(var)
            print var
        f.close()
        newf.close()
        return path
    def __generatemeizixulie(self,mainpath,meiziurllist):
        path=mainpath+'meizixulie.txt'
        f=open(path,'w')
        for meiziurl in meiziurllist:
            f.write(meiziurl[1])
            f.write('\n')
        f.close()
        return path
    def generatemeizidirs(self):
        mainpath=self.mainpath
        path=self.__formatxulie()
        f=open(path,'r')  
        for dirs in f.readlines():
            dirs=dirs.rstrip("\n")
            temp=mainpath+dirs
            if os.path.exists(temp):
              #  print temp
                pass
            else:            
                os.makedirs(mainpath+dirs)
                print True
        return path 



