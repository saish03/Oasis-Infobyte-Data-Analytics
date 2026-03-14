import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- HEADER ----------------

st.title("📊 Data Analytics Project Dashboard")
st.markdown("An interactive platform for exploring multiple data analytics projects and visual insights.")

# ---------------- SIDEBAR ----------------

st.sidebar.title("📂 Navigation")

page = st.sidebar.radio(
    "Select Project",
    [
        "🏠 Home",
        "📈 Retail Sales Analysis",
        "👥 Customer Segmentation",
        "🏡 House Price Analysis",
        "🍷 Wine Quality Analysis"
    ]
)

# ---------------- HOME ----------------

if page == "🏠 Home":

    st.markdown("## 🚀 Interactive Data Analytics Platform")

    st.write(
        """
        Welcome to the **Data Analytics Dashboard**, an interactive environment designed to explore
        multiple datasets using modern data visualization and analytics techniques.

        This platform demonstrates how data can be transformed into meaningful insights using
        **Python, machine learning, and interactive visualization tools**.
        """
    )

    st.markdown("---")

    # KPI CARDS
    st.subheader("📊 Project Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📁 Total Projects", "5")

    with col2:
        st.metric("📊 Data Analytics Projects", "3")

    with col3:
        st.metric("🤖 Machine Learning Projects", "2")

    with col4:
        st.metric("🧰 Tools Used", "6+")

    st.markdown("---")

    # PROJECT CARDS
    st.subheader("📚 Projects Included in the Dashboard")

    c1, c2 = st.columns(2)

    with c1:

        st.info("📈 **Retail Sales Analysis**")
        st.write(
            """
            Analyze retail transaction data to uncover **sales patterns, category performance,
            and distribution trends** using visual analytics.
            """
        )

        st.info("👥 **Customer Segmentation**")
        st.write(
            """
            Identify customer groups based on **income, spending behavior,
            and purchasing patterns** to support targeted marketing strategies.
            """
        )

    with c2:

        st.info("🏡 **House Price Analysis**")
        st.write(
            """
            Explore housing market data to understand **price distributions,
            property characteristics, and market trends**.
            """
        )

        st.info("🍷 **Wine Quality Analysis**")
        st.write(
            """
            Investigate chemical features of wine to determine **how different
            properties influence quality ratings**.
            """
        )

    st.markdown("---")

    # TECHNOLOGY SECTION
    st.subheader("🛠 Technology Stack")

    t1, t2, t3, t4, t5 = st.columns(5)

    t1.success("Python")
    t2.success("Pandas")
    t3.success("Plotly")
    t4.success("Scikit-Learn")
    t5.success("Streamlit")

    st.markdown("---")

    # FEATURES SECTION
    st.subheader("✨ Dashboard Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.write("📊 **Interactive Visualizations**")
        st.write("Dynamic charts that allow zooming, filtering, and exploration.")

    with f2:
        st.write("⚡ **Real-Time Data Exploration**")
        st.write("Instant analysis of datasets with responsive UI components.")

    with f3:
        st.write("📱 **Responsive Dashboard Layout**")
        st.write("Optimized layout with sidebar navigation and interactive panels.")

    st.markdown("---")

    st.success("💡 Use the **sidebar navigation** to explore each analytics project and interact with the visualizations.")

# ---------------- RETAIL SALES ----------------

elif page == "📈 Retail Sales Analysis":

    st.header("Retail Sales Dashboard")

    df = pd.read_csv("Datasets/retail_sales.csv")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    if len(numeric_cols) > 0 and len(cat_cols) > 0:

        x_col = cat_cols[0]
        y_col = numeric_cols[0]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Category Distribution")
            fig = px.bar(df, x=x_col, y=y_col, color=x_col)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Sales Distribution")
            fig2 = px.histogram(df, x=y_col)
            st.plotly_chart(fig2, use_container_width=True)

# ---------------- CUSTOMER SEGMENTATION ----------------

elif page == "👥 Customer Segmentation":

    st.header("Customer Segmentation Analysis")

    df = pd.read_csv("Datasets/mall_customers.csv")

    st.dataframe(df.head(), use_container_width=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_cols) >= 2:

        x_col = numeric_cols[0]
        y_col = numeric_cols[1]

        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            color=y_col,
            size=y_col,
            title="Customer Segmentation Scatter Plot"
        )

        st.plotly_chart(fig, use_container_width=True)

# ---------------- HOUSE PRICE ----------------

elif page == "🏡 House Price Analysis":

    st.header("House Price Analytics")

    df = pd.read_csv("Datasets/house_prices.csv")

    st.dataframe(df.head(), use_container_width=True)

    price_cols = [col for col in df.columns if "price" in col.lower()]

    if len(price_cols) > 0:

        price_col = price_cols[0]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Price Distribution")
            fig = px.histogram(df, x=price_col, nbins=40)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Price Box Plot")
            fig2 = px.box(df, y=price_col)
            st.plotly_chart(fig2, use_container_width=True)

# ---------------- WINE QUALITY ----------------

elif page == "🍷 Wine Quality Analysis":

    st.header("Wine Quality Dataset")

    df = pd.read_csv("Datasets/wine_quality.csv")

    st.dataframe(df.head(), use_container_width=True)

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_cols) >= 2:

        x_col = numeric_cols[0]
        y_col = numeric_cols[-1]

        col1, col2 = st.columns(2)

        with col1:
            fig = px.scatter(
                df,
                x=x_col,
                y=y_col,
                color=y_col,
                title="Feature vs Wine Quality"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig2 = px.histogram(df, x=y_col)
            st.plotly_chart(fig2, use_container_width=True)

# ---------------- FOOTER ----------------

st.markdown("---")
st.caption("Interactive Data Analytics Dashboard")