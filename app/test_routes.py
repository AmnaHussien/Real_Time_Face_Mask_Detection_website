from app import app

def test_existing_routes():
    tester = app.test_client()

    # Test Home Route
    response = tester.get('/')
    print("Home:", response.status_code, response.data[:50])

    # Test Detect Route
    response = tester.get('/detect')
    print("Detect:", response.status_code, response.data[:50])

    # Test Unfinished Routes (should give 404)
    response = tester.get('/results')
    print("Results:", response.status_code)
    response = tester.get('/about')
    print("About:", response.status_code)

if __name__ == "__main__":
    test_existing_routes()