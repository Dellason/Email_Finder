from fastapi import FastAPI
import requests

app = FastAPI(
    title="Hunter.io Email Finder API",
    description="A simple API to find email addresses using Hunter.io",
    version="1.0.0"
)

HUNTER_API_KEY = " "

# Endpoint for finding emails
@app.get("/find-email/")
async def find_email(
    first_name: str,
    last_name: str,
    domain: str,
):
   
    hunter_api_key = HUNTER_API_KEY
    
    # Hunter.io API endpoint
    url = "https://api.hunter.io/v2/email-finder"
    
    # Parameters for the request
    params = {
        'first_name': first_name,
        'last_name': last_name,
        'domain': domain,
        'api_key': hunter_api_key
    }
    
    # Make request to Hunter.io
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise exception for HTTP errors

    data = response.json()
    email = data.get('data', {}).get('email')
    
    if email:
        return {"email": email}
    else:
        return {"email": None, "message": "No email found"}


# Root endpoint
@app.get("/")
async def root():
    """Welcome to the Hunter.io Email Finder API"""
    return {
        "message": "Welcome to the Hunter.io Email Finder API",
        "usage": "Make a GET request to /find-email/ with first_name, last_name, and domain parameters"
    }

