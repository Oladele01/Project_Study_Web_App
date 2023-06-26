import cv2 as cv
import streamlit as st
from streamlit_image_comparison import image_comparison


header = st.container()     #Add title and subtitle to the main interface of the app
images = st.container()
contours = st.container()
particle_size = st.container()
contour_detection = st.container()

to_do = st.container()



with header:
    st.title("CONTOUR DETECTION WITHIN BULK SOLIDS VIA IMAGE PROCESSING METHODS")
    st.markdown("####Description of the project bullshit")

with images:
    st.header("These are the images I used in this project")
    st.text("jhbcu bcuhabc beiucb bruhaha")

    st.subheader("One Cent Coin")
    st.text("This is the BGR colour palette image of the one cent coin")
    image_read = cv.imread('coin.jpeg')
    st.image(image_read)

    st.subheader("One Cent Coin")
    st.text("This is the BGR colour palette image of the one cent coin")
    image = cv.cvtColor(image_read, cv.COLOR_BGR2RGB)
    st.image(image)

    st.subheader("One Cent Coin")
    st.text("This is the BGR colour palette image of the one cent coin")
    image_copy1 = image.copy()
    gray_scale = cv.cvtColor(image_copy1, cv.COLOR_RGB2GRAY)
    st.image(gray_scale)

    st.subheader("One Cent Coin")
    st.text("This is the BGR colour palette image of the one cent coin")
    gray_scale_inverted = cv.bitwise_not(gray_scale)
    st.image(gray_scale_inverted)

    st.subheader("One Cent Coin")
    st.text("This is the BGR colour palette image of the one cent coin")
    _, binary_threshold = cv.threshold(gray_scale_inverted, 100, 255, cv.THRESH_BINARY)
    st.image(binary_threshold)

    st.subheader("One Cent Coin")
    st.text("This is the BGR colour palette image of the one cent coin")
    canny_edges = cv.Canny(image, 120, 170)
    st.image(canny_edges)

    image_comparison1 = image_comparison(
        img1=image_read,
        img2=image,
        label1="text1",
        label2="text1",
        width=700,
        starting_position=50,
        show_labels=True,
        make_responsive=True,
        in_memory=True,
    )
    image_comparison2 = image_comparison(
        img1=binary_threshold,
        img2=canny_edges,
    )



with contour_detection:
    st.header("CONTOUR DETECTION")
    st.markdown("jnicbnucedbuhjbcnd")

with contours:
    st.header("CONTOURS")

with particle_size:
    st.header("PARTICLE SIZE")

with to_do:
    st.header("TO-DO")

#Add sidebar to the app
st.sidebar.markdown("# My Awesome Project Study Data App")
st.sidebar.markdown("### Author: \n Oladele, Segun Olabanji")

st.sidebar.markdown("Welcome to my first awesome app. This app is built using Streamlit and uses data source from redfin housing market data. I hope you enjoy!")