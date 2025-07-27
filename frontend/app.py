import streamlit as st
import requests
import pandas as pd

st.title("Reco-AI-Agent")

# Fetch products
response = requests.get("http://localhost:8000/products/")
products = response.json()
df = pd.DataFrame(products)
st.dataframe(df[["name", "description", "quantity"]])

# Vendor dropdown
response = requests.get("http://localhost:8000/vendors/")
vendors = response.json()
vendor_names = {v["name"]: v["id"] for v in vendors}
vendor = st.selectbox("Select Vendor", list(vendor_names.keys()))

# Fetch vendor products
if vendor:
    vendor_id = vendor_names[vendor]
    response = requests.get(f"http://localhost:8000/vendors/{vendor_id}")
    vendor_products = response.json()
    df_vendor = pd.DataFrame(vendor_products)
    st.dataframe(df_vendor[["name", "description", "quantity"]])

    # Product selection for recommendation
    product_names = {p["name"]: p["id"] for p in vendor_products}
    product = st.selectbox("Select Product", list(product_names.keys()))
    
    if product:
        product_id = product_names[product]
        if st.button("Get Recommendation"):
            response = requests.get(f"http://localhost:8000/recommendations/{product_id}/{vendor_id}")
            recommendation = response.json()["recommendation"]
            st.write(f"**Recommendation**: {recommendation}")

# Review form
st.subheader("Submit a Review")
product_id = st.number_input("Product ID", min_value=1, step=1)
rating = st.slider("Rating", 1, 5, 3)
comment = st.text_area("Comment")
if st.button("Submit Review"):
    review_data = {"product_id": product_id, "rating": rating, "comment": comment}
    response = requests.post("http://localhost:8000/reviews/", json=review_data)
    if response.status_code == 200:
        st.success("Review submitted!")
    else:
        st.error("Error submitting review.")
