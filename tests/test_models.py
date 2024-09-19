#def test_model_route_model_id(client):
#  res = client.get('/api/models/', query_string = {'model_id': 'cc2078aa'})
#  assert res.status_code == 200
#
#  data = res.get_json()
#  assert data[0]['model_id'] == 'cc2078aa'

def test_model_route_country(client):
  res = client.get('/api/models/', query_string = {'country': 'US,CA'})

  assert res.status_code == 200