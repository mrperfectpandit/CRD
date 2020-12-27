import threading 
from threading import*
import time

#'dic' is the dictionary in which we store data
dic={} 

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dic:
        print("error: this key already exists")
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1020*1024) and value<=(16*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    temp1=[value,timeout]
                else:
                    temp1=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dic[key]=temp1
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key name! key_name must contain only alphabets and no number or special character")

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dic:
        print("error: given key does not exist in database. try another ")
    else:
        temp2=dic[key]
        if temp2[1]!=0: #b[1] show time index
            if time.time()<temp2[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(temp2[0]) #return jasonObject
                return stri
            else:
                print("error: time to live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(temp2[0])
            return stri

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dic:
        print("error: given key does not exist in database. try another") 
    else:
        temp2=dic[key]
        if temp2[1]!=0:
            if time.time()<temp2[1]: #comparing the current time with expiry time
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error: time to live of",key,"has expired") 
        else:
            del dic[key]
            print("key is successfully deleted")
