def test_model_route(client):
  res = client.get('/api/models/', query_string = {'model_id': 'cc2078aa'})

  assert res.status_code == 200

  data = res.get_json()
  assert data[0]['model_id'] == 'cc2078aa'