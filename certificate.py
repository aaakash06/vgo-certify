import cv2
import os
import base64
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageFont


font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
activities = ["Get certificate","About"]
st.sidebar.image("images/logo.png", )
choice=st.sidebar.selectbox("Select Activty",activities)
root_path = os.path.dirname(__file__) + '/'

contributions = {
    "Nirpa Gautam": ["article", "Thriving Together" ],
    "Sarojina Subedi": ["article", "Butterfly as a Pollinator" ],
    "Abash Kaphle": ["article", "Future Trend of Pollinators" ],
    "Suman Neupane": ["article", "Industrial Revolution to Organic Revival" ],
       "Satya Bhattarai": ["article", "Floriculture, Pollinators, and Biodiversity" ],
       "Shubheksha Sharma": ["article", "Thriving Together" ],
       "Aananda Pandey": ["peom", "Floriculture For Future" ],
       "Dharma Acharya": ["peom", "The Garden of Friendship" ],
    #    "Binita Chaudhari": ["article", "फूल खेतीमा जैविक मलको महत्व, चुनौती र समाधान" ],
}


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}"> Download {file_label}</a>'
    return href

def annotate(name):
 
    st.write("Your certificate is ready.")
    if os.path.isfile("Certificates/Certificate_{}.jpg".format(name)):
        original = cv2.imread("Certificates/Certificate_{}.jpg".format(name))
        st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',output_format='PNG')
        st.markdown(get_binary_file_downloader_html("Certificates/Certificate_{}.jpg".format(name), 'Certificate'), unsafe_allow_html=True)
        return
    # st.markdown(f"**{clicked} clicked**" )

    # the path will be default to the defualt image
    path = "certificate_templates/OriginalFormat.png"

    
    certi = cv2.imread(path)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    font=7
    # get boundary of this text
    textsize = cv2.getTextSize(name, font, fontScale, 3)[0]
    
    # get coords based on boundary
    textX = (certi.shape[1] - textsize[0]) // 2
    textY = (certi.shape[0] + textsize[1]) // 2

    original = cv2.putText(certi, name, (textX, 642),font, fontScale, (0, 0, 0), thickness=3)    
    
    # writing the description
    typee = contributions[name][0]
    title = contributions[name][1] 
    desc = f"{typee} titled \"{title}.\""
    origin =(881,720)
    green_rgb= (10, 93, 46)
    green_hex = "#0a5d2e"
    font_path = "Arial.ttf"
    font_size = 100
    size = None
    font = ImageFont.truetype(root_path+font_path, font_size)
    img_pill = Image.fromarray(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pill)
    box = ((881, 722, 1805, 765))
    # draw.rectangle(box, outline="#000")
    while (size is None or size[2]-size[0] > (box[2] - box[0]) or size[3]-size[1] > (box[3] - box[1])) and font_size > 0:
        font = ImageFont.truetype(font_path, font_size)
        size = draw.textbbox((box[0], box[1]), desc, font=font)
        font_size -= 1
    font = ImageFont.truetype(font_path, font_size+2)
    draw.text((box[0],box[1]), desc, fill=green_rgb, font=font)       
    original = cv2.cvtColor(np.array(img_pill), cv2.COLOR_RGB2BGR)
    
    cv2.imwrite("Certificates/Certificate_{}.jpg".format(name),original)
    
    if st.button("View certificate"):
        st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',output_format='PNG')
        st.markdown(get_binary_file_downloader_html("Certificates/Certificate_{}.jpg".format(name), 'Certificate'), unsafe_allow_html=True)


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
    st.markdown("connect with me (https://www.linkedin.com/in/aakash-bagale/)")


