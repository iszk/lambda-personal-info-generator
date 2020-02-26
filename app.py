import json
from chalice import Chalice
from chalicelib import dummy

app = Chalice(app_name='dummydata')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/random_lead')
def random_lead():
    # qp = app.current_request.query_params
    # 何が設定できたら嬉しい？
    #   個数(0-2くらい？)
    # state = app.current_request.query_params['state']
    lead = dummy.get_random_lead()

    return json.dumps(lead, ensure_ascii=False)
