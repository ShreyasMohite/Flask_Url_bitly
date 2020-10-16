from flask import Flask,url_for,redirect,render_template,request,session
import bitly_api 


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    try:
        que=[]       
        name=request.form.get('urls')
        if name:

            BITLY_ACCESS_TOKEN = "access_token"  #your bitly access token
            b = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN) 
            response = b.shorten(uri=name)
            urlss={
                'names':response['url']
            }
            que.append(urlss)
        else:
            pass
    except Exception as e:
        print(e)

    return render_template("home.html",name=que)




if __name__ == "__main__":
    app.run(debug=True,host="192.168.1.204")