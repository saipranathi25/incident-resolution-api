from fastapi import FastAPI

app = FastAPI()

incidents = {
    "INC001": {
        "summary": "User unable to login to internal application portal.",
        "root_cause": "Expired authentication session and cached credentials caused login failure.",
        "resolution_steps": [
            "Ask the user to clear browser cache and cookies.",
            "Restart authentication service.",
            "Verify user credentials in identity provider.",
            "Check network connectivity to application server.",
            "Restart application service if issue persists."
        ]
    }
}

@app.get("/resolution/{incident_id}")
def get_resolution(incident_id: str):

    if incident_id in incidents:
        return incidents[incident_id]

    return {"message": "Incident not found"}