import azure.functions as func
import logging
import pandas as pd
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger_recommendation")
def http_trigger_recommendation(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    top_nn=pd.read_pickle('top_n.pkl')
    userId = req.params.get('userId')
    if not userId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userId = req_body.get('userId')

    if userId:
        top_n=top_nn[int(userId)]
        
        return func.HttpResponse(json.dumps({
            'top_n': top_n
        }))
            #f"Hello, {top_n}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a userId in the query string or in the request body for a personalized response.",
             status_code=200
        )