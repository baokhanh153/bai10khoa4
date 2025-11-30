import streamlit as st
audio = open('nhac_nha_hang_nhat.mp3', 'rb')
st.audio(audio, format='audio/mp3')
image = 'Nha_hang_nhat.jpeg'
st.image(image, caption='nhà hàng')
mon_khai_vi = ['Bánh mì áp chảo', 'Cháo trai trai', 'Cà pháo', 'Súp rau củ', 'Kim bắc','Trứng cút lộn xào me']
mon_chinh = ['Cơm giang dưa bò', 'Phở Bò', 'Phở gà', 'vịt quay', ' Rau cải xào thịt', 'tôm hùm nướng bơ', 'Chim xào hột vịt']
mon_trang_mieng = ['Kem việt quất', 'Cốc chè ngũ sắc', 'Nước sinh tố', 'Nước chanh', 'Cà phê sữa(đá)']

with st.form('Thực đơn yêu thích'):
	options1 = st.multiselect( 'Món khai vị ưa thích của bạn?', mon_khai_vi)
	options2 = st.multiselect( 'Món chính ưa thích của bạn?', mon_chinh)
	options3 = st.multiselect( 'Món tráng miệng ưa thích của bạn?', mon_trang_mieng)
	submitted = st.form_submit_button('Submit')
	if submitted:
		st.write('Các lựa chọn của bạn là:')
		st.write('**1. Món khai vị:**')
		if len(options1) == 0:
			st.write('Bạn chưa chọn món khai vị')
		else:
			for i in range(len(options1)):
				st.write(options1[i])
		st.write('**2. Món chính**')
		if len(options2) == 0:
			st.write('Bạn chưa chọn món chính')
		else:
			for i in range(len(options2)):
				st.write(options2[i])

		st.write('**3. Món tráng miệng**')
		if len(options3) == 0:
			st.write('Bạn chưa chọn món tráng miệng')
		else:
			for i in range(len(options3)):
				st.write(options3[i])