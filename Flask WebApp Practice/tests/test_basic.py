from flask_basic_webapp import create_app


def test_index():
    app = create_app()
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Flask Basic WebApp' in resp.data
