from graders import grade_action

TASKS = [
    {
        "email_id": "e1",
        "sender": "billing@company.com",
        "subject": "Payment failed",
        "body": "Customer payment did not go through.",
        "gold": {
            "classification": "billing",
            "priority": "high",
            "decision": "escalate",
        },
        "graders": [grade_action],
    },
    {
        "email_id": "e2",
        "sender": "calendar@company.com",
        "subject": "Team meeting tomorrow",
        "body": "Please confirm your availability.",
        "gold": {
            "classification": "meeting",
            "priority": "medium",
            "decision": "schedule",
        },
        "graders": [grade_action],
    },
    {
        "email_id": "e3",
        "sender": "promo@randomsite.com",
        "subject": "Win a free phone now!!!",
        "body": "Click here now.",
        "gold": {
            "classification": "spam",
            "priority": "low",
            "decision": "archive",
        },
        "graders": [grade_action],
    }
]