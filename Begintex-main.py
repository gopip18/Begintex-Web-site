# Begintex-main.py
import streamlit as st
from Latex_Services import show_latex_services
import pandas as pd

# Set up the Streamlit page configuration
st.set_page_config(page_title="BeginTex Website", layout="wide")

# Sidebar Menu Navigation
st.sidebar.title("BeginTex Navigation")
menu_options = ["🏠 Home", "🛠️ LaTeX Services", "🌠 About Us", "📧 Contact"]
menu_selection = st.sidebar.radio("Select a Page:", menu_options)

# Home Page Content
if menu_selection == "🏠 Home":
    st.title("🏠 Welcome to BeginTex")
    st.markdown("""
        ## Welcome to Our LaTeX Support Services!

        Are you a student or researcher looking for professional LaTeX support to format your academic documents? We specialize in providing high-quality LaTeX assistance tailored to your specific needs. From structuring complex academic papers to handling intricate equations and formatting, we are here to help you create polished, publication-ready documents.

        ### Our Services:

        ### **1. Journal Paper LaTeX Formatting**
        We provide complete LaTeX support for formatting journal papers according to the requirements of top academic publishers. Whether it’s handling complex references, equations, tables, or figures, we ensure that your manuscript meets the strict guidelines of academic journals.

        ### **2. Thesis and Dissertation LaTeX Structuring**
        Our team offers expert LaTeX support for thesis and dissertation formatting, ensuring proper chapter structures, bibliography management, and seamless integration of figures and tables. We follow university-specific templates and guidelines, so your thesis or dissertation is formatted to perfection.

        ### **3. Conference Paper LaTeX Formatting**
        Preparing a conference paper? We can help you structure and format your document in LaTeX according to the specific style and requirements of various academic conferences, ensuring your paper is ready for submission.

        ### **4. Book and Monograph LaTeX Support**
        Whether it’s a technical book, monograph, or chapter, we provide comprehensive LaTeX support for long-form documents. We handle complex content formatting, cross-references, indexing, and bibliography management to help you create a professional-quality book.

        ### **5. Article and Report LaTeX Formatting**
        Need to format an academic article or report? We assist with LaTeX structuring, citation management, and formatting to ensure your work is well-organized and visually appealing.

        ### Why Choose Us?
        - **LaTeX Expertise:** We have extensive experience in LaTeX formatting and technical structuring, making even the most complex documents look clean and professional.
        - **Customized Formatting Solutions:** Each service is tailored to your document’s unique requirements, ensuring precise formatting and organization.
        - **Student-Friendly Approach:** We provide specialized LaTeX support for students and researchers, helping you focus on your content while we take care of the formatting.

        ### Get Started Today!
        Are you a student looking for professional LaTeX formatting support for your journal, thesis, dissertation, conference paper, book, or article? We are here to help. Contact us now to discuss how we can make your LaTeX document stand out with our expert support!     
        
    """)

# About Us Page Content
elif menu_selection == "🌠 About Us":
    st.title("🌠 About BeginTex")
    st.markdown("""
        ### Who We Are
        Welcome to Begintex, the innovative company that’s changing the way industry operates. Founded in 2023, we’re on a mission to goal. Our team is comprised of experts in LaTeX, and we’re passionate about your team.

        At Begintex, we believe in core values, which guide everything we do.Our goal is to become the leading niche provider, and we’re committed to achieving this by strategy. We believe that our combination of unique strengths will set us apart from our competitors and allow us to succeed.

        Thank you for considering Begintex for your niche needs. We’re excited to show you what we can do, and we look forward to serving you in the future.
    """)

# LaTeX Services Page - Import from Latex_Services.py
elif menu_selection == "🛠️ LaTeX Services":
    show_latex_services()

# Contact Page Content
elif menu_selection == "📧 Contact":
    st.title("📧 Contact Us")
    st.markdown("""
        **Email**: vendorgopi@gmail.com 
        
    """)
#**Phone**: +91 9940613610
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content { background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.write("🔗 **Quick Links**")
st.sidebar.markdown("[Visit Our Website](https://www.begintex.com)")
st.sidebar.markdown("[Support](mailto:info@begintex.com)")

# WhatsApp Contact Option in Sidebar
st.sidebar.markdown("### 📞 Contact Us on WhatsApp")
whatsapp_number = "+919940613610"  # Replace with your actual WhatsApp number (without '+' sign)
whatsapp_url = f"https://wa.me/{whatsapp_number}"
st.sidebar.markdown(
    f"""
    <a href="{whatsapp_url}" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp Logo" width="50"/>
    </a>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("### 📊 Analytics Data")

# Handle the absence of the JSON file and display a friendly message
try:
    # Try reading the analytics data from the JSON file
    analytics_data = pd.read_json("usage_data.json")
    # Display the data in the sidebar as a dataframe
    st.sidebar.dataframe(analytics_data)
except FileNotFoundError:
    # If the file is not found, display a message in the sidebar
    st.sidebar.write("No analytics data available yet. Please generate some data.")
except ValueError:
    # Handle other JSON parsing errors gracefully
    st.sidebar.write("Analytics data is not properly formatted.")