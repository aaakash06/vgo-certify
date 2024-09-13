import cv2
import os
import base64
import streamlit as st


font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
activities = ["Get certificate","About"]
st.sidebar.image("images\\logo.png")
choice=st.sidebar.selectbox("Select Activty",activities)


contributions = {
    "Nirpa Gautam": ["article", "Thriving Together" ],
    "Sarojina Subedi": ["article", "Butterfly as a Pollinator" ],
    "Abash Kaphle": ["article", "Future Trend of Pollinators" ],
    "Suman Neupane": ["article", "Industrial Revolution to Organic Revival" ],
       "Satya Bhattarai": ["article", "Floriculture, Pollinators, and Biodiversity" ],
       "Shubheksha Sharma": ["article", "Thriving Together" ],
       "Aananda Pandey": ["peom", "Floriculture For Future" ],
       "Dharma Acharya": ["peom", "The Garden of Friendship" ],
       "Binita Chaudhari": ["article", "" ],
}


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"> Download {file_label}</a>'
    return href

def annotate(name):
 
    st.write("Your certificate is ready.")
    # st.markdown(f"**{clicked} clicked**" )

    # the path will be default to the defualt image
    path = "certificate_templates\\OriginalFormat.png"

    
    certi = cv2.imread(path)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # get boundary of this text
    textsize = cv2.getTextSize(name, font, fontScale, 5)[0]

    # get coords based on boundary
    textX = (certi.shape[1] - textsize[0]) // 2
    textY = (certi.shape[0] + textsize[1]) // 2

    original = cv2.putText(certi, name, (textX, 642),font,   fontScale, (0, 0, 0), thickness=5)    
    cv2.imwrite("Certificate_{}.jpg".format(name),original)

    
    if st.button("View certificate"):
        st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',output_format='PNG')
        st.markdown(get_binary_file_downloader_html("Certificate_{}.jpg".format(name), 'Certificate'), unsafe_allow_html=True)


if choice =="Get certificate":
    
    st.title("Get Your Certificate")
    recipient_name=st.selectbox("Name",[""]+[key for key in contributions])
    if len(recipient_name)>0:
        annotate(recipient_name)
    else:
        st.write("Please enter Your name in the Above Field To download the Certificate")    
    #st.markdown(get_binary_file_downloader_html(original, 'Picture'), unsafe_allow_html=True)


if choice =="About":
    st.subheader("Cerficate App")
    st.markdown("</> by Aakash" )
    st.markdown("connect with me 😃 (https://www.linkedin.com/in/aakash-bagale/)")
