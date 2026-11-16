from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
MODELS = ROOT / "models"


def models_ready() -> bool:
    needed = [
        DATA / "WBCD_dataset.csv",
        DATA / "clean_metabric.csv",
        MODELS / "model_a.pkl",
        MODELS / "model_b.pkl",
        MODELS / "model_c.pkl",
    ]
    return all(path.exists() for path in needed)


@st.cache_data
def load_wbcd() -> pd.DataFrame:
    return pd.read_csv(DATA / "WBCD_dataset.csv")


@st.cache_data
def load_metabric() -> pd.DataFrame:
    return pd.read_csv(DATA / "clean_metabric.csv")
