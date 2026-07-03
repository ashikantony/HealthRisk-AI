"""
HealthRisk AI
Data Acquisition Package

Contains all data ingestion pipelines for:

1. MIMIC-IV Clinical Data
2. WHO Epidemiological Data
3. ClinicalTrials.gov Data
4. FDA FAERS Data
5. CMS Claims Data
6. CDC Public Health Data
7. Financial Market Data
"""

from .base_loader import BaseLoader
from .mimic_downloader import MIMICDownloader
from .who_api_loader import WHOAPILoader
from .clinical_trials_loader import ClinicalTrialsLoader
from .fda_faers_loader import FDAFAERSLoader
from .cms_loader import CMSLoader
from .cdc_loader import CDCLoader
from .financial_data_loader import FinancialDataLoader
from .data_validation import DataValidator

__all__ = [
    "BaseLoader",
    "MIMICDownloader",
    "WHOAPILoader",
    "ClinicalTrialsLoader",
    "FDAFAERSLoader",
    "CMSLoader",
    "CDCLoader",
    "FinancialDataLoader",
    "DataValidator",
]