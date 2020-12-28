import os
from posenet.singleImageDet import getDet
from pose.getAppropriateObject import getObject
from copy import deepcopy
import cv2

def getRefs(excercise:str,conf):
    refFolder=".\\references\\"+excercise
    lst=list(os.listdir(refFolder))
    lst=[m for m in lst if "frame" in m]
    lst.sort()
    refs=[]
    cnt=0
    for j in lst:
        de,image=getDet(refFolder+"\\"+j)
        obj=deepcopy(getObject(excercise,de,conf))
        obj.addMoreInfo(cv2.imread(refFolder+"\\"+j),None,cnt,None)
        refs.append(obj)
        cnt+=1
    return refs