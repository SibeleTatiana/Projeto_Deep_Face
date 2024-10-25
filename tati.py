from deepface import DeepFace
from PIL import Image, ImageDraw
import streamlit as st
import os
from PIL import Image

def main():

    st.title('My app')

    menu = ['Carregar', 'Ver imagens', 'Outros']

    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Carregar':
        image_file = st.file_uploader('Upload Files', type=['png', 'jpeg'])
        if image_file is not None:
            img = Image.open(image_file)

            with open(os.path.join('album/', image_file.name),'wb') as f:
                f.write((image_file).getbuffer())
            st.success('File Saved')

            objs = DeepFace.extract_faces(
                img_path='album/' + image_file.name,
                detector_backend='opencv',
                align=True,
            )

            top_left = (objs[0]['facial_area']['x'], objs[0]['facial_area']['y'])  # X, Y coordinates of the top-left corner
            bottom_right = (objs[0]['facial_area']['x'] + objs[0]['facial_area']['w'], objs[0]['facial_area']['y'] + objs[0]['facial_area']['h'])  # X, Y coordinates of the bottom-right corner
            draw = ImageDraw.Draw(img)
            draw.rectangle([top_left, bottom_right], outline='green', width=2)
            st.image(img, width=500)

            cropped_image = img.crop([*top_left, *bottom_right])
            cropped_image.save('rosto_nao_identificado/nova.jpg')

        st.text('Carregar')

    elif choice =='Ver imagens':
        # images = []
        # for filename in os.listdir('./', filename)
        #     if filename.lower().endswith(('.png','jpg','jpeg','tiff','.images.append(filename'))
        st.text('Ver imagens')

    elif choice == 'Outros':

        st.text('Outros')

#
#
# objs[0]['region']
#
# image = Image.open(path)
# draw = ImageDraw.Draw(image)
#
# top_left = (objs[0]['region']['x'], objs[0]['region']['y'])  # X, Y coordinates of the top-left corner
# bottom_right = (objs[0]['region']['x'] + objs[0]['region']['w'], objs[0]['region']['y'] + objs[0]['region']['h'])  # X, Y coordinates of the bottom-right corner
# draw.rectangle([top_left, bottom_right], outline='green', width=20)
#
# plt.imshow(image)
# plt.axis('off')
# plt.show()
#
#
# plt.imshow(cropped_image)
# plt.axis('off')
# plt.show()
# face_objs
main()

