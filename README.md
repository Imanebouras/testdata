# Lead Generation Tool

This repository contains a complete Python lead generation tool for business prospecting using user-provided Google Maps links. The tool processes and organizes business data effectively, allows for customization, and has a simple user interface.

## Features
- Input handling for multiple Google Maps business links and manual business entry.
- Business data extraction and normalization (name, phone number, website).
- Moroccan phone normalization to international format (+212).
- CSV storage and Google Sheets API synchronization.
- Duplicate detection and removal.
- Support for tagging leads.
- WhatsApp link generation and pre-filled message capabilities.
- User-defined message templates with business-name personalization.
- Easy-to-use Streamlit UI or CLI, including table view for leads.
- Export functionality for CSV and Excel files.
- Bonus features include lead status updates (new, contacted, replied), notes section, and search/filtering options.

## Directory Structure
```
lead_generation_tool/
│
├── lead_gen.py           # Main script for running the lead generation tool.
├── utils.py              # Helper functions for normalization, APIs, etc.
├── api_handler.py        # Functions for handling Google Sheets API.
├── scrapers/             # Contains code for data extraction (from user input)
│   ├── business_scraper.py  # Logic to extract business data
│   └── ...                  # Any future scrapers
├── templates/            # Contains message templates.
│   ├── template_1.txt       # Example template.
│   └── ...                  # Additional templates
├── requirements.txt      # Required dependencies.
└── README.md             # Documentation for users.
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Imanebouras/testdata.git
   cd testdata
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Run the main script:
   ```bash
   python lead_gen.py
   ```
- Enter Google Maps links or manual business entries as prompted.
- Follow on-screen instructions to extract and normalize business data.

## Dependencies
- streamlit
- pandas
- openpyxl
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client

Feel free to extend this tool and customize it to fit your needs!
