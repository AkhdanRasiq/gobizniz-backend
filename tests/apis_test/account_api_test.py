def test_create_account(client):
    data = {"name":"testuser", "email":"testuser@nofoobar.com"}
    response = client.post("/api/v1/account/", json=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"

def test_get_all_accounts(client):
    response = client.get("/api/v1/account/all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
