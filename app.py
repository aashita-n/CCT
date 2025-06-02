from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

CLOUD_DATA = {
    "compute": {
        "AWS": [
            {
                "name": "t3.nano",
                "vcpu": 2,
                "memory": 0.5,
                "storage": "EBS Only",
                "price": 0.0052,
                "region": "us-east-1",
                "family": "General Purpose"
            },
            {
                "name": "t3.micro",
                "vcpu": 2,
                "memory": 1,
                "storage": "EBS Only",
                "price": 0.0104,
                "region": "us-east-1",
                "family": "General Purpose"
            },
            {
                "name": "t3.small",
                "vcpu": 2,
                "memory": 2,
                "storage": "EBS Only",
                "price": 0.0208,
                "region": "us-east-1",
                "family": "General Purpose"
            },
            {
                "name": "t3.medium",
                "vcpu": 2,
                "memory": 4,
                "storage": "EBS Only",
                "price": 0.0416,
                "region": "us-east-1",
                "family": "General Purpose"
            },
            {
                "name": "m5.large",
                "vcpu": 2,
                "memory": 8,
                "storage": "EBS Only",
                "price": 0.096,
                "region": "us-east-1",
                "family": "General Purpose"
            },
            {
                "name": "m5.xlarge",
                "vcpu": 4,
                "memory": 16,
                "storage": "EBS Only",
                "price": 0.192,
                "region": "us-east-1",
                "family": "General Purpose"
            },
            {
                "name": "c5.large",
                "vcpu": 2,
                "memory": 4,
                "storage": "EBS Only",
                "price": 0.085,
                "region": "us-east-1",
                "family": "Compute Optimized"
            },
            {
                "name": "r5.large",
                "vcpu": 2,
                "memory": 16,
                "storage": "EBS Only",
                "price": 0.126,
                "region": "us-east-1",
                "family": "Memory Optimized"
            },
            {
                "name": "g4dn.xlarge",
                "vcpu": 4,
                "memory": 16,
                "storage": "125 GB NVMe SSD",
                "price": 0.526,
                "region": "us-east-1",
                "family": "GPU Instances"
            }
        ],
        "Azure": [
            {
                "name": "B1s",
                "vcpu": 1,
                "memory": 1,
                "storage": "SSD",
                "price": 0.008,
                "region": "eastus",
                "family": "Burstable"
            },
            {
                "name": "B2s",
                "vcpu": 2,
                "memory": 4,
                "storage": "SSD",
                "price": 0.034,
                "region": "eastus",
                "family": "Burstable"
            },
            {
                "name": "D2s v3",
                "vcpu": 2,
                "memory": 8,
                "storage": "SSD",
                "price": 0.096,
                "region": "eastus",
                "family": "General Purpose"
            },
            {
                "name": "D4s v3",
                "vcpu": 4,
                "memory": 16,
                "storage": "SSD",
                "price": 0.192,
                "region": "eastus",
                "family": "General Purpose"
            },
            {
                "name": "F2s v2",
                "vcpu": 2,
                "memory": 4,
                "storage": "SSD",
                "price": 0.085,
                "region": "eastus",
                "family": "Compute Optimized"
            },
            {
                "name": "E2s v3",
                "vcpu": 2,
                "memory": 16,
                "storage": "SSD",
                "price": 0.126,
                "region": "eastus",
                "family": "Memory Optimized"
            },
            {
                "name": "NC6s v3",
                "vcpu": 6,
                "memory": 112,
                "storage": "SSD",
                "price": 1.98,
                "region": "eastus",
                "family": "GPU Optimized"
            }
        ],
        "GCP": [
            {
                "name": "e2-micro",
                "vcpu": 2,
                "memory": 1,
                "storage": "SSD",
                "price": 0.0086,
                "region": "us-central1",
                "family": "General Purpose"
            },
            {
                "name": "e2-small",
                "vcpu": 2,
                "memory": 2,
                "storage": "SSD",
                "price": 0.0172,
                "region": "us-central1",
                "family": "General Purpose"
            },
            {
                "name": "e2-medium",
                "vcpu": 2,
                "memory": 4,
                "storage": "SSD",
                "price": 0.0344,
                "region": "us-central1",
                "family": "General Purpose"
            },
            {
                "name": "n2-standard-2",
                "vcpu": 2,
                "memory": 8,
                "storage": "SSD",
                "price": 0.0971,
                "region": "us-central1",
                "family": "General Purpose"
            },
            {
                "name": "n2-standard-4",
                "vcpu": 4,
                "memory": 16,
                "storage": "SSD",
                "price": 0.1942,
                "region": "us-central1",
                "family": "General Purpose"
            },
            {
                "name": "c2-standard-4",
                "vcpu": 4,
                "memory": 16,
                "storage": "SSD",
                "price": 0.2088,
                "region": "us-central1",
                "family": "Compute Optimized"
            },
            {
                "name": "m2-ultramem-4",
                "vcpu": 4,
                "memory": 256,
                "storage": "SSD",
                "price": 1.4598,
                "region": "us-central1",
                "family": "Memory Optimized"
            },
            {
                "name": "n1-standard-1",
                "vcpu": 1,
                "memory": 3.75,
                "storage": "SSD",
                "price": 0.0475,
                "region": "us-central1",
                "family": "Legacy"
            }
        ]
    },
    "storage": {
        "AWS": [
            {
                "name": "S3 Standard",
                "type": "Object Storage",
                "price_per_gb": 0.023,
                "durability": "99.999999999%",
                "availability": "99.99%",
                "region": "us-east-1",
                "class": "Standard"
            },
            {
                "name": "S3 Infrequent Access",
                "type": "Object Storage",
                "price_per_gb": 0.0125,
                "durability": "99.999999999%",
                "availability": "99.9%",
                "region": "us-east-1",
                "class": "Infrequent Access"
            },
            {
                "name": "S3 Glacier",
                "type": "Object Storage",
                "price_per_gb": 0.004,
                "durability": "99.999999999%",
                "availability": "99.99% (after restore)",
                "region": "us-east-1",
                "class": "Archive"
            },
            {
                "name": "EBS gp3",
                "type": "Block Storage",
                "price_per_gb": 0.08,
                "durability": "99.8-99.9%",
                "availability": "99.9%",
                "region": "us-east-1",
                "class": "General Purpose"
            },
            {
                "name": "EBS io1",
                "type": "Block Storage",
                "price_per_gb": 0.125,
                "durability": "99.8-99.9%",
                "availability": "99.9%",
                "region": "us-east-1",
                "class": "Provisioned IOPS"
            },
            {
                "name": "EFS Standard",
                "type": "File Storage",
                "price_per_gb": 0.30,
                "durability": "99.999999999%",
                "availability": "99.9%",
                "region": "us-east-1",
                "class": "Standard"
            }
        ],
        "Azure": [
            {
                "name": "Blob Storage Hot",
                "type": "Object Storage",
                "price_per_gb": 0.018,
                "durability": "99.999999999%",
                "availability": "99.9%",
                "region": "eastus",
                "class": "Hot"
            },
            {
                "name": "Blob Storage Cool",
                "type": "Object Storage",
                "price_per_gb": 0.01,
                "durability": "99.999999999%",
                "availability": "99%",
                "region": "eastus",
                "class": "Cool"
            },
            {
                "name": "Blob Storage Archive",
                "type": "Object Storage",
                "price_per_gb": 0.002,
                "durability": "99.999999999%",
                "availability": "99.9% (after rehydrate)",
                "region": "eastus",
                "class": "Archive"
            },
            {
                "name": "Managed Disks Standard HDD",
                "type": "Block Storage",
                "price_per_gb": 0.04,
                "durability": "99.9%",
                "availability": "99.9%",
                "region": "eastus",
                "class": "Standard HDD"
            },
            {
                "name": "Managed Disks Premium SSD",
                "type": "Block Storage",
                "price_per_gb": 0.15,
                "durability": "99.9%",
                "availability": "99.9%",
                "region": "eastus",
                "class": "Premium SSD"
            },
            {
                "name": "Azure Files Standard",
                "type": "File Storage",
                "price_per_gb": 0.06,
                "durability": "99.999999999%",
                "availability": "99.9%",
                "region": "eastus",
                "class": "Standard"
            }
        ],
        "GCP": [
            {
                "name": "Standard Storage",
                "type": "Object Storage",
                "price_per_gb": 0.02,
                "durability": "99.999999999%",
                "availability": "99.95%",
                "region": "us-central1",
                "class": "Standard"
            },
            {
                "name": "Nearline Storage",
                "type": "Object Storage",
                "price_per_gb": 0.01,
                "durability": "99.999999999%",
                "availability": "99%",
                "region": "us-central1",
                "class": "Nearline"
            },
            {
                "name": "Coldline Storage",
                "type": "Object Storage",
                "price_per_gb": 0.004,
                "durability": "99.999999999%",
                "availability": "99%",
                "region": "us-central1",
                "class": "Coldline"
            },
            {
                "name": "Archive Storage",
                "type": "Object Storage",
                "price_per_gb": 0.0012,
                "durability": "99.999999999%",
                "availability": "99% (after restore)",
                "region": "us-central1",
                "class": "Archive"
            },
            {
                "name": "Persistent SSD",
                "type": "Block Storage",
                "price_per_gb": 0.17,
                "durability": "99.9%",
                "availability": "99.9%",
                "region": "us-central1",
                "class": "SSD"
            },
            {
                "name": "Persistent HDD",
                "type": "Block Storage",
                "price_per_gb": 0.04,
                "durability": "99.9%",
                "availability": "99.9%",
                "region": "us-central1",
                "class": "HDD"
            },
            {
                "name": "Filestore Standard",
                "type": "File Storage",
                "price_per_gb": 0.20,
                "durability": "99.999999999%",
                "availability": "99.9%",
                "region": "us-central1",
                "class": "Standard"
            }
        ]
    }
}



@app.route('/')
def index():
    return render_template('index.html', 
                         last_updated=datetime.now().strftime("%Y-%m-%d"),
                         providers=["AWS", "Azure", "GCP"],
                         regions={
                             "AWS": ["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"],
                             "Azure": ["eastus", "westus", "northeurope", "southeastasia"],
                             "GCP": ["us-central1", "us-west1", "europe-west1", "asia-southeast1"]
                         })

@app.route('/compare', methods=['POST'])
def compare():
    service_type = request.form.get('service_type', 'compute')
    selected_providers = request.form.getlist('providers')
    selected_regions = request.form.getlist('regions')
    min_vcpu = int(request.form.get('min_vcpu', 0)) if service_type == 'compute' else None
    min_memory = float(request.form.get('min_memory', 0)) if service_type == 'compute' else None
    max_price = float(request.form.get('max_price', float('inf')))
    
    if not selected_providers:
        selected_providers = ["AWS", "Azure", "GCP"]
    
    results = {}
    for provider in selected_providers:
        if provider in CLOUD_DATA[service_type]:
            items = CLOUD_DATA[service_type][provider]
            
            # Apply filters
            filtered_items = []
            for item in items:
                region_match = not selected_regions or item['region'] in selected_regions
                
                if service_type == 'compute':
                    vcpu_match = min_vcpu is None or item['vcpu'] >= min_vcpu
                    memory_match = min_memory is None or item['memory'] >= min_memory
                    price_match = item['price'] <= max_price
                    
                    if region_match and vcpu_match and memory_match and price_match:
                        filtered_items.append(item)
                else:  # storage
                    price_match = item['price_per_gb'] <= max_price
                    
                    if region_match and price_match:
                        filtered_items.append(item)
            
            if filtered_items:
                results[provider] = filtered_items
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)