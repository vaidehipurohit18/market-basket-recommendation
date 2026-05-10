# ---------------------------------------------------
# IMPORT LIBRARIES
# ---------------------------------------------------

import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Market Basket Recommendation System",
    layout="wide"
)

# ---------------------------------------------------
# LOAD RULES
# ---------------------------------------------------

rules = joblib.load("association_rules.pkl")

# ---------------------------------------------------
# CLEAN RULES
# ---------------------------------------------------

rules['antecedents'] = rules['antecedents'].apply(
    lambda x: list(x)
)

rules['consequents'] = rules['consequents'].apply(
    lambda x: list(x)
)

# ---------------------------------------------------
# EXTRACT PRODUCTS
# ---------------------------------------------------

products = set()

for items in rules['antecedents']:
    for item in items:
        products.add(item)

for items in rules['consequents']:
    for item in items:
        products.add(item)

products = sorted(list(products))

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("Market Basket Recommendation Dashboard")

st.markdown("""
Select products to generate dynamic product recommendations using Association Rule Mining.
""")

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("Shopping Cart")

selected_products = st.sidebar.multiselect(
    "Add Products",
    products
)

# ---------------------------------------------------
# DISPLAY CART
# ---------------------------------------------------

st.subheader("Selected Products")

if selected_products:

    cart_df = pd.DataFrame({
        "Products in Cart": selected_products
    })

    st.dataframe(
        cart_df,
        width='stretch'
    )

else:

    st.info("Select products from the sidebar.")

# ---------------------------------------------------
# RECOMMENDATION ENGINE
# ---------------------------------------------------

recommendations = []

for _, row in rules.iterrows():

    antecedents = row['antecedents']

    consequents = row['consequents']

    # Count matching selected products
    matches = len(
        set(selected_products).intersection(set(antecedents))
    )

    # Only recommend if rule strongly matches
    if matches > 0:

        for item in consequents:

            if item not in selected_products:

                recommendations.append({
                    "Recommended Product": item,
                    "Confidence": round(row['confidence'], 2),
                    "Lift": round(row['lift'], 2),
                    "Matched Products": matches
                })

# ---------------------------------------------------
# RECOMMENDATION PROCESSING
# ---------------------------------------------------

if recommendations:

    rec_df = pd.DataFrame(recommendations)

    # Aggregate duplicate recommendations
    rec_df = rec_df.groupby(
        'Recommended Product',
        as_index=False
    ).agg({
        'Confidence': 'max',
        'Lift': 'max',
        'Matched Products': 'max'
    })

    # Sort by:
    # 1. matched products
    # 2. lift
    # 3. confidence

    rec_df = rec_df.sort_values(
        by=[
            'Matched Products',
            'Lift',
            'Confidence'
        ],
        ascending=False
    )

    # ---------------------------------------------------
    # DISPLAY RECOMMENDATIONS
    # ---------------------------------------------------

    st.subheader("Recommended Products")

    st.dataframe(
        rec_df,
        width='stretch'
    )

    # ---------------------------------------------------
    # DYNAMIC ADD BUTTONS
    # ---------------------------------------------------

    st.subheader("Quick Add Recommendations")

    cols = st.columns(3)

    for idx, row in rec_df.head(9).iterrows():

        with cols[idx % 3]:

            st.markdown(f"""
            ### {row['Recommended Product']}

            Confidence: {row['Confidence']}

            Lift: {row['Lift']}
            """)

else:

    if selected_products:

        st.warning(
            "No recommendations found."
        )

# ---------------------------------------------------
# RULES TABLE
# ---------------------------------------------------

st.divider()

st.subheader("Association Rules")

display_rules = rules.copy()

display_rules['antecedents'] = display_rules[
    'antecedents'
].astype(str)

display_rules['consequents'] = display_rules[
    'consequents'
].astype(str)

st.dataframe(
    display_rules,
    width='stretch'
)

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.divider()

st.subheader("Business Insights")

st.markdown("""
This recommendation system identifies products frequently purchased together using the Apriori Algorithm.

Applications include:

- Cross-selling
- Product recommendations
- Retail analytics
- Customer purchase behavior analysis
- Inventory optimization
""")