import docker

client = docker.from_env()
def deploy_test_container():
    res = client.containers.run("debian","echo hello world")
    print(res)
    return res

def service_scaling(alert_service_name, up=True):
    # Get service based-on alert_service_name
    # Check service deploy mode: Only scalable if mode is Replicated
    # Retrieve parameters from service labels and current replicas
    # Scale up/down service
    if (alert_service_name == "${app}"):
        print("Grafana webhook template error: "+alert_service_name)
        return 1
    alert_service_name = "demo_"+alert_service_name
    print("Service:" + alert_service_name)
    alert_service = client.services.list(filters = {"name":alert_service_name})[0]
    if("Replicated" in alert_service.attrs["Spec"]["Mode"]):
        alert_service_scale_current = int(alert_service.attrs["Spec"]["Mode"]["Replicated"]["Replicas"])
        alert_service_labels = alert_service.attrs["Spec"]["TaskTemplate"]["ContainerSpec"]["Labels"]
        alert_service_scale_each = 1
        alert_service_scale_max = 5
        alert_service_scale_min = 1
        if("label.scale.max" in alert_service_labels):
            alert_service_scale_max = int(alert_service_labels["label.scale.max"])
        if("label.scale.min" in alert_service_labels):
            alert_service_scale_min = int(alert_service_labels["label.scale.min"])
        if("label.scale.each" in alert_service_labels):
            alert_service_scale_each = int(alert_service_labels["label.scale.each"])
        if(up):
            alert_service_scale_after = alert_service_scale_current + alert_service_scale_each
            if (alert_service_scale_after > alert_service_scale_max):
                print("Service can't scale up")
                return "Service can't scale up"
            else:
                print("Scaling up: " + alert_service_name)
                return alert_service.scale(alert_service_scale_after)
        else:
            alert_service_scale_after = alert_service_scale_current - alert_service_scale_each
            if (alert_service_scale_after < alert_service_scale_min):
                print("Service can't scale down")
                return "Service can't scale down"
            else:
                print("Scaling down: "+ alert_service_name)
                return alert_service.scale(alert_service_scale_after)
    else:
        return "Service can't scale"

def new_func():
    return 0

