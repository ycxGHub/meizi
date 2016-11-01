'''


@author: ycx
'''
import urllib2
import re
class SrcUrlUtil(object):
       
    def __init__(self,url,mainpath,*mainurllist):
        self.url=url
        self.mainpath=mainpath
        self.mainurllist=mainurllist
    def findUrllistSrcUrl(self):
        header={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.5"}
        for i,srcUrl in enumerate(self.mainurllist):
            print srcUrl
            if srcUrl.endswith('/'):            
                print True
                html=''
                
            else:   
                print 'scuss'
                req=urllib2.Request(self.url+srcUrl,headers=header)
                print self.url+srcUrl
                rep=urllib2.urlopen(req)
                html=rep.read()
                srcnumbers=self.findHtmlSrcUrl(html)
                self.outputsrcnumbers(self.mainpath+srcUrl, srcnumbers[0])
                s=raw_input('')              
            
    def  findHtmlSrcUrl(self,html): 
        ruler='<a href=.http://[^\/]*/\d+/(\d\d).'
        reg=re.compile(ruler)
        srcnumbers=re.findall(reg, html)
        print srcnumbers
        return srcnumbers
    def outputsrcnumbers(self,path,content):
        path=path+'\srcnumbers.txt'
        f=open(path,'w')
        f.write(content)
        f.close()
        return path