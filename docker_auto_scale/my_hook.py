from flask import Flask, request, json
import my_handler

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World'

@app.route('/test', methods = ['POST'])
def hook_handle():
    
    #print((request.json))
    req = (request.json)
    
    # Process Alert title
    alert_title_label = req["title"].split()[0]
    if ( alert_title_label == "[Alerting]" ):
    # Process Alert tags
        if ("tags" in req):
            alert_tags = req["tags"]
            if("node" in alert_tags):
                if (alert_tags["node"] == "1"):
                    return my_handler.deploy_test_container()

            if("service-app" in alert_tags):
                if (alert_tags["service-app"] == "1"):
                    print(req)
                    if (alert_tags["isScaleUp"]=="1"):
                      return my_handler.service_scaling(req["message"], True)
                    else:
                      return my_handler.service_scaling(req["message"], False)

    return alert_title_label


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
