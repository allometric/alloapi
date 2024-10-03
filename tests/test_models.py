def test_model_route(client):
  res = client.get(
    '/model/aaaaaaa'
  )

  assert res.status_code == 200

  data = res.get_json()
  assert data['_id'] == 'aaaaaaa'

def test_models_route_setquals(client):
  res = client.post(
    '/models/',
    json = {
      'descriptors.region': {'$all': ['US-OR', 'US-WA'], '$size': 2}
    }
  )

  assert res.status_code == 200