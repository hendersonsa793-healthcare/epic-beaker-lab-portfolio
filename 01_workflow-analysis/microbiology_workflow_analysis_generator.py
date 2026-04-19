#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
Microbiology workflow analysis dataset generator
Portfolio section: 01_workflow-analysis

Purpose
-------
Generate a synthetic microbiology / molecular dataset that models the
order-to-result lifecycle in an Epic Beaker-aligned lab workflow project.

This version is intentionally framed for the workflow-analysis section of the
portfolio. It emphasizes:
- order -> collect -> receive -> instrument result -> final result
- turnaround-time segmentation
- event flags for workflow bottlenecks
- location- and priority-driven delay patterns

Use Case
--------
This dataset is designed to simulate real-world Epic Beaker workflow investigations,
where analysts evaluate turnaround time (TAT), identify delays, and troubleshoot
order-to-result lifecycle issues across clinical locations and priorities.

Analysis Applications
---------------------
This dataset can be used to:
- Identify transport delays by location
- Compare STAT vs Routine TAT performance
- Detect pre-analytic vs analytic bottlenecks
- Simulate Epic Clarity-style reporting queries
"""

from __future__ import annotations

import random
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------

OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "microbiology_workflow_analysis_dataset.csv"
NUM_ORDERS = 1500
LOOKBACK_DAYS = 30
RANDOM_SEED = 42

random.seed(RANDOM_SEED)


# ---------------------------------------------------------------------
# REFERENCE DATA
# ---------------------------------------------------------------------

TEST_CATALOG = [
    {
        "test_name": "COVID/Flu PCR",
        "department": "Molecular",
        "instrument": "ID NOW",
        "specimen_type": "Nasal Swab",
        "workflow_type": "Molecular",
    },
    {
        "test_name": "C. Diff PCR",
        "department": "Molecular",
        "instrument": "Revogene",
        "specimen_type": "Stool",
        "workflow_type": "Molecular",
    },
    {
        "test_name": "Respiratory Panel",
        "department": "Molecular",
        "instrument": "BioFire",
        "specimen_type": "Nasopharyngeal Swab",
        "workflow_type": "Molecular",
    },
    {
        "test_name": "Blood Culture",
        "department": "Microbiology",
        "instrument": "BACTEC",
        "specimen_type": "Blood",
        "workflow_type": "Culture",
    },
    {
        "test_name": "Urine Culture",
        "department": "Microbiology",
        "instrument": "Manual Culture",
        "specimen_type": "Urine",
        "workflow_type": "Culture",
    },
    {
        "test_name": "Wound Culture",
        "department": "Microbiology",
        "instrument": "Manual Culture",
        "specimen_type": "Wound",
        "workflow_type": "Culture",
    },
    {
        "test_name": "MRSA Screen",
        "department": "Microbiology",
        "instrument": "BD Max",
        "specimen_type": "Nasal Swab",
        "workflow_type": "Molecular",
    },
]

PATIENT_LOCATIONS = ["ICU", "ED", "MedSurg", "Oncology", "FSED", "PrimaryCare"]
PRIORITIES = ["STAT", "Routine"]


# ---------------------------------------------------------------------
# DATA MODEL
# ---------------------------------------------------------------------

@dataclass
class WorkflowOrder:
    order_id: int
    patient_location: str
    priority: str
    test_name: str
    department: str
    instrument: str
    specimen_type: str
    workflow_type: str
    order_time: datetime
    collect_time: datetime
    receive_time: datetime
    instrument_result_time: datetime
    final_result_time: datetime
    downstream_post_status: str
    verification_status: str
    result_status: str


# ---------------------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------------------

def random_order_time() -> datetime:
    """Generate a random order time within the last N days."""
    now = datetime.now()
    days_back = random.randint(0, LOOKBACK_DAYS - 1)
    minutes_back = random.randint(0, 23 * 60 + 59)
    return now - timedelta(days=days_back, minutes=minutes_back)


def get_collection_delay(location: str, priority: str) -> int:
    """Return specimen collection delay in minutes."""
    if priority == "STAT":
        return random.randint(5, 30)

    if location in ["ICU", "ED"]:
        return random.randint(10, 45)
    if location == "FSED":
        return random.randint(20, 90)
    if location == "PrimaryCare":
        return random.randint(30, 180)
    return random.randint(15, 90)


def get_transport_delay(location: str, priority: str) -> int:
    """Return specimen transport / receipt delay in minutes."""
    if priority == "STAT":
        if location in ["ICU", "ED"]:
            return random.randint(5, 20)
        if location == "FSED":
            return random.randint(30, 120)
        return random.randint(15, 60)

    if location in ["ICU", "ED"]:
        return random.randint(10, 40)
    if location == "FSED":
        return random.randint(60, 240)
    if location == "PrimaryCare":
        return random.randint(120, 480)
    return random.randint(20, 90)


def get_lab_processing_delay(test_name: str, workflow_type: str, priority: str) -> int:
    """Return lab processing delay in minutes."""
    if workflow_type == "Molecular":
        if priority == "STAT":
            return random.randint(30, 120)
        return random.randint(60, 240)

    if test_name == "Blood Culture":
        return random.randint(720, 2880)   # 12-48 hours
    if test_name == "Urine Culture":
        return random.randint(1080, 2880)  # 18-48 hours
    if test_name == "Wound Culture":
        return random.randint(1440, 4320)  # 24-72 hours

    return random.randint(60, 240)


def get_result_post_delay() -> tuple[int, str]:
    """
    Simulate a light downstream result-posting delay.

    This keeps a bridge to future system-integration work without making
    middleware/interface logic the main focus of this project.
    """
    roll = random.random()

    if roll < 0.92:
        return random.randint(1, 10), "posted_on_time"
    if roll < 0.98:
        return random.randint(15, 60), "delayed_posting"
    return random.randint(60, 240), "manual_follow_up"


def get_verification_status(workflow_type: str, downstream_post_status: str) -> str:
    """Return auto/manual verification status."""
    if downstream_post_status == "manual_follow_up":
        return "Manual"

    if workflow_type == "Molecular":
        return random.choices(["Auto", "Manual"], weights=[75, 25], k=1)[0]

    return random.choices(["Auto", "Manual"], weights=[25, 75], k=1)[0]


def get_result_status(downstream_post_status: str) -> str:
    """Return final result status."""
    if downstream_post_status == "manual_follow_up":
        return random.choice(["Corrected", "Final"])
    return random.choice(["Preliminary", "Final"])


# ---------------------------------------------------------------------
# GENERATION LOGIC
# ---------------------------------------------------------------------

def build_orders(num_orders: int = NUM_ORDERS) -> pd.DataFrame:
    """Generate the synthetic workflow dataset."""
    orders: list[dict] = []

    for order_id in range(1, num_orders + 1):
        test = random.choice(TEST_CATALOG)
        location = random.choice(PATIENT_LOCATIONS)
        priority = random.choices(PRIORITIES, weights=[20, 80], k=1)[0]

        order_time = random_order_time()
        collect_time = order_time + timedelta(
            minutes=get_collection_delay(location, priority)
        )
        receive_time = collect_time + timedelta(
            minutes=get_transport_delay(location, priority)
        )
        instrument_result_time = receive_time + timedelta(
            minutes=get_lab_processing_delay(
                test_name=test["test_name"],
                workflow_type=test["workflow_type"],
                priority=priority,
            )
        )

        result_post_delay, downstream_post_status = get_result_post_delay()
        final_result_time = instrument_result_time + timedelta(minutes=result_post_delay)

        verification_status = get_verification_status(
            workflow_type=test["workflow_type"],
            downstream_post_status=downstream_post_status,
        )
        result_status = get_result_status(downstream_post_status)

        order = WorkflowOrder(
            order_id=order_id,
            patient_location=location,
            priority=priority,
            test_name=test["test_name"],
            department=test["department"],
            instrument=test["instrument"],
            specimen_type=test["specimen_type"],
            workflow_type=test["workflow_type"],
            order_time=order_time,
            collect_time=collect_time,
            receive_time=receive_time,
            instrument_result_time=instrument_result_time,
            final_result_time=final_result_time,
            downstream_post_status=downstream_post_status,
            verification_status=verification_status,
            result_status=result_status,
        )

        orders.append(asdict(order))

    return pd.DataFrame(orders)


# ---------------------------------------------------------------------
# DERIVED METRICS
# ---------------------------------------------------------------------

def add_workflow_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add segmented turnaround-time metrics."""
    df = df.copy()

    df["tat_collection_min"] = (
        df["collect_time"] - df["order_time"]
    ).dt.total_seconds() / 60

    df["tat_transport_min"] = (
        df["receive_time"] - df["collect_time"]
    ).dt.total_seconds() / 60

    df["tat_lab_min"] = (
        df["instrument_result_time"] - df["receive_time"]
    ).dt.total_seconds() / 60

    df["tat_result_post_min"] = (
        df["final_result_time"] - df["instrument_result_time"]
    ).dt.total_seconds() / 60

    df["tat_total_min"] = (
        df["final_result_time"] - df["order_time"]
    ).dt.total_seconds() / 60
    
    df["stat_delay_flag"] = df.apply(
    lambda row: "Y" if row["priority"] == "STAT" and row["tat_total_min"] > 180 else "N",
    axis=1
    )

    
    df["tat_total_hours"] = df["tat_total_min"] / 60
    return df

# Event flags simulate threshold-based alerts commonly used in
# Epic Clarity reporting and operational dashboards to identify delays

def add_event_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Add event-style workflow flags for bottleneck detection."""
    df = df.copy()

    df["collection_delay_flag"] = df["tat_collection_min"].apply(
        lambda x: "Y" if x > 60 else "N"
    )
    df["transport_delay_flag"] = df["tat_transport_min"].apply(
        lambda x: "Y" if x > 120 else "N"
    )
    df["lab_delay_flag"] = df["tat_lab_min"].apply(
        lambda x: "Y" if x > 240 else "N"
    )
    df["result_post_delay_flag"] = df["tat_result_post_min"].apply(
        lambda x: "Y" if x > 30 else "N"
    )
    df["stat_delay_flag"] = df.apply(
    lambda row: "Y" if row["priority"] == "STAT" and row["tat_total_min"] > 180 else "N",
    axis=1
    )

    return df


# ---------------------------------------------------------------------
# EXPORT + QA
# ---------------------------------------------------------------------

def export_dataset(df: pd.DataFrame, output_file: Path = OUTPUT_FILE) -> None:
    """Write dataset to CSV."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)


def run_data_quality_checks(df: pd.DataFrame) -> None:
    """Display quick validation checks."""
    print("Rows generated:", len(df))
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nSample rows:")
    print(df.head())

    print("\nAverage TAT by location (hours):")
    print(df.groupby("patient_location")["tat_total_hours"].mean().round(2))

    print("\nDownstream post status counts:")
    print(df["downstream_post_status"].value_counts())

    print(f"\nCSV exported as: {OUTPUT_FILE}")


def main() -> None:
    df = build_orders()
    df = add_workflow_metrics(df)
    df = add_event_flags(df)
    export_dataset(df)
    run_data_quality_checks(df)


if __name__ == "__main__":
    main()


# In[ ]:




