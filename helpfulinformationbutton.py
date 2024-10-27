import streamlit as st
import pandas as pd
import numpy as np

left, middle, right = st.columns(3)
if left.button("Water Testing Kits", use_container_width=True):
    left.markdown("Home water testing kits are readily available in stores and are used to test water for contaminants. They test for things like pH, hardness, chlorine, nitrates, and bacteria.")
    df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.33,
        "col2": np.random.randn(1000) / 50 + -121.89,
    }
    )
    st.map(df, latitude="col1", longitude="col2")
if middle.button("Boiling Test", use_container_width=True):
    middle.markdown("You can boil water for more than a minute to kill off most harmfull bacteria that may be in the water. Boiling won't get rid of heavy metals or chemical contaminants that may be in the water.")
if right.button("Smell and Look test", use_container_width=True):
    right.markdown("The smell and look of the water can be an indicator of quality. Cloudiness can show that the water has high mineral content or contamination. Rotten egg smell can indicate bacteria or hydrogen sulfide.")