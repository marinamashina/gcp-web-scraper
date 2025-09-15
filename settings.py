#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Google Cloud configuration
GOOGLE_APPLICATION_CREDENTIALS = "/Users/marina.kurmanova/Documents/Hackathon/sunny-resolver-472119-a0-e58a0d5472ac.json"

# Google Cloud Project Configuration
BIGQUERY_PROJECT_ID = "sunny-resolver-472119-a0"
BIGQUERY_DATASET_ID = "web_scrapped_data"
BIGQUERY_TABLE_NAME = "fake_job_data"
BIGQUERY_LOCATION = "europe-west1"  # e.g., "europe-west8"

# Web Scraping Configuration
JOB_BOARD_URL = "https://realpython.github.io/fake-jobs/"
PAGE_LOAD_DELAY = 2  # Seconds to wait for page to load