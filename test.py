'''


@author: ycx
'''
import urllib
from url import meiziUrl
from srcurl import SrcUrlUtil
if __name__ == '__main__':
    i=raw_input('print page numbers:')
    mainpath='D:/photo/python/meizi/page/'+i+'/'
    url='http://www.mzitu.com/page/'+i
    meiziUrl1=meiziUrl(url,mainpath)
    mainUrllistpath=meiziUrl1.generatemeizidirs()
    f=open(mainUrllistpath,'r')
    url='http://www.mzitu.com/'
    mainUrllist=[]
    for var in f.readlines():
        var=var.rstrip()
        print var
        mainUrllist.append(var)

 
    src=SrcUrlUtil(url,mainpath,*mainUrllist)
    src.findUrllistSrcUrl()
    src.findUrllistSrcUrl()
 
    
    