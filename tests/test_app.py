def test_create_user(client):
    response = client.post('/users', json={'name': 'Test User', 'email': 'test@example.com', 'phone_number': '1234567890'})
    assert response.status_code == 201
    assert response.json['message'] == 'User created successfully!'
