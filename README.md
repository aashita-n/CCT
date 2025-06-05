# CloudCompare: A Multi-Cloud Comparison Tool

CloudCompare is a responsive and user-friendly web application that allows seamless comparison of compute and storage services from major cloud providers — AWS, Azure, and Google Cloud Platform (GCP). Built using Python (Flask), HTML/CSS, and JavaScript, the platform simplifies cloud service decision-making with a clean UI and powerful filtering capabilities.

Live Demo: [https://cct-8d1r.onrender.com](https://cct-8d1r.onrender.com)  
Supports both desktop and mobile browsers.

---

## Problem Statement

With the vast offerings from AWS, Azure, and GCP, choosing the right compute or storage service can be confusing due to:

- Inconsistent terminologies
- Varied pricing models
- Scattered documentation

CloudCompare solves this by presenting all relevant service information in a centralized, standardized, and filterable format.

---

## Objectives

- Build a user-friendly web application to compare cloud services.
- Provide standardized and comprehensive information across AWS, Azure, and GCP.
- Implement dynamic filters based on vCPU, memory, price, and region.
- Gain hands-on experience in full-stack development and deployment.
- Simulate realistic cloud service decisions using structured data.
- Deploy on a cloud-native platform (Render) to showcase hosting skills.
- Keep the design modular to allow future API integrations.

---

## Features

- Real-time filtering of services by vCPU, memory, price, and region
- Side-by-side comparison across AWS, Azure, and GCP
- Responsive design for desktop and mobile screens
- Built using Flask (backend) and HTML/CSS/JS (frontend)
- Hosted live on Render

---

## Tech Stack

| Layer       | Tools and Technologies                        |
|-------------|-----------------------------------------------|
| Backend     | Python, Flask, Gunicorn                       |
| Frontend    | HTML, CSS (Bootstrap), JavaScript (Fetch API)|
| Data        | Static JSON (cloud_data.json)                 |
| DevOps      | Git, GitHub                                   |
| Deployment  | Render                                        |


---

## Running Locally

To run this project on your local machine:

```bash
# Clone the repository
git clone https://github.com/your-username/cloudcompare.git
cd cloudcompare

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask app
python app.py

```
---

## Future Enhancements
- Integration with live APIs for real-time cloud data
- User authentication system
- Advanced analytics and reporting dashboards
- Addition of more service types and cloud providers
