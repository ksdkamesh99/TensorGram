import keras
from urllib import request
from urllib.parse import quote
import requests
import io
import matplotlib.pyplot as plt


class TensorGram(keras.callbacks.Callback):
  
  def __init__(self,modelname,id):
    self.modelname=modelname
    self.id=id
    self.attributes={}
    self.key_attributes=[]
  def parse_url(self,t):
    t=t.split(' ')
    t='%20'.join(t)
    return t
  def on_train_begin(self, logs=None):
    self.text="Model "+self.modelname+" Training Started"
    self.text=str(self.text)
    url="https://ksdkamesh99.pythonanywhere.com/send?id="+str(self.id)+"&data="+self.parse_url(self.text)
    s=request.urlopen(url)


  def on_train_end(self, logs=None):
    self.text="Model "+self.modelname+" Traning Completed"
    self.text=str(self.text)
    url="https://ksdkamesh99.pythonanywhere.com/send?id="+str(self.id)+"&data="+self.parse_url(self.text)
    s=request.urlopen(url)
    for i in self.key_attributes:
      self.image_buff(self.attributes[i],i)

  def on_epoch_begin(self, epoch, logs=None):
    self.text="Model "+self.modelname+" Epoch "+str(epoch+1)+" Running"
    self.text=str(self.text)
    url="https://ksdkamesh99.pythonanywhere.com/send?id="+str(self.id)+"&data="+self.parse_url(self.text)
    s=request.urlopen(url)

  def on_epoch_end(self, epoch, logs=None):
    self.text="Model "+self.modelname+" loss after epoch "+str(epoch+1)+" is "+str(logs.get('loss'))
    self.text=str(self.text)
    if epoch==0:
      self.key_attributes=list(logs.keys())
      for i in self.key_attributes:
        self.attributes[i]=[]
    for i in self.key_attributes:
      self.attributes[i].append(logs.get(i))
    url="https://ksdkamesh99.pythonanywhere.com/send?id="+str(self.id)+"&data="+self.parse_url(self.text)
    s=request.urlopen(url)
  def image_buff(self,attri,title):
    plt.figure()
    plt.plot(attri)
    plt.title(title)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    files={'photo':buf.getbuffer()}
    url="https://ksdkamesh99.pythonanywhere.com/sendphoto?id="+str(self.id)+"&caption="+title
    ss=requests.post(url,files=files)




