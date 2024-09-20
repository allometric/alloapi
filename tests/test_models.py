def test_model_route_model_id(client):
  res = client.post(
    '/api/models/',
    json = {
      'model_id': 'cc2078aa'
    }
  )

  assert res.status_code == 200

  data = res.get_json()
  assert data[0]['model_id'] == 'cc2078aa'

def test_model_route_setquals(client):
  res = client.post(
    '/api/models/',
    json = {
      'descriptors.region': {'$all': ['US-OR', 'US-WA'], '$size': 2}
    }
  )

  assert res.status_code == 200