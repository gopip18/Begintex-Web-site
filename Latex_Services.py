# Latex_Services.py
import streamlit as st

def show_latex_services():
    """
    Function to display the LaTeX services section in Streamlit.
    It shows a title and a markdown list of offered services.
    """
    st.title("Our LaTeX Services")

    st.markdown("""
        Word to LaTex
        -------------

        Are you struggling to convert your Word document to LaTeX format? Look no further than our Word to LaTeX conversion service. We offer high-quality, accurate conversions that will help you achieve the professional-looking document you need.

        The company’s Word to LaTeX converter has many features, such as the ability to convert almost any type of document from Microsoft Word into LaTeX format. Our company meets all of the Journal Style Guide and follows all the Template Instructions. If you are looking for a trusted Word to LaTeX conversion service provider, then we are here to help you.
    """)
    st.image("Begintex-w2t.jpg", width=600)
    st.markdown("""
    LaTex Formatting
    ----------------

    Follow your target journal’s formatting guidelines: the formatting team will modify your manuscript’s layout, title, author, affiliation, table placement, illustrations placement, and citations/references to meet the requirements of your Journals and Books
   
    Specializations:
    
    ✅Journal Header Information: Customizing headers and footers to match journal specifications.
    
    ✅Citations and References: Ensuring accurate citation styles and reference formatting.
    
    ✅Tables and Illustrations: Expert placement and formatting of tables and figures.
    
    ✅Equation Editing and Alignment: Precise formatting and alignment of mathematical equations.
    
    ✅Layout Management: Proficient in both single-column and double-column layouts.
    
    ✅Reference Styles: Experienced with APA, APS, MathPhysSci, and Vancouver styles.I am highly versatile in the TeX platform and can adapt templates according to specific requirements. Providing a style guide enhances the efficiency and accuracy of formatting, ensuring error-free documents.
    
    """
    )

    st.markdown("""
    Track Changes Management
    -------------------------
    
    Implemented and managed track changes in LaTeX documents, facilitating clear and transparent editing and collaboration among team members.
    """)

if __name__ == "__main__":
    show_latex_services()
