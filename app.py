import streamlit as st
from pathlib import Path
import pandas as pd
st.set_page_config(page_title="Rehabilitation ML Dashboard",layout="wide")
st.title("Rehabilitation ML Results Dashboard")
st.caption("Interactive view of derived, leakage-safe evaluation outputs from the master's practical ML projects.")
base=Path(__file__).parent / "data"
files=sorted(base.glob("*.csv")) if base.exists() else []
if not files:
 st.info("Add derived CSV result files to the data/ folder to populate the dashboard.")
else:
 choice=st.selectbox("Result table",[p.name for p in files]); df=pd.read_csv(base/choice); st.dataframe(df,use_container_width=True)
 st.download_button("Download selected table",df.to_csv(index=False),choice,"text/csv")
