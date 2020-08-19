from  PIL import Image , ImageFilter , ImageShow
import sys
import ntpath
import os
#  print ()
# load images from folder 
# convert png to jpg
# resize pics 
# attach all image to each card
# save in a folder
default_card = "H:/Cards Anime/card.png"

sub_folder = ["clover","spade","heart","diamond",]

every_iter = ["number","symbol"]

main_folder = "H:/Cards Anime"

current_folder_count = 0  

i=0

j = 0

output_folder = "H:/Cards Anime/created_cards/"

for current_directory in os.listdir(main_folder):

	full_path = main_folder + "/" + sub_folder[current_folder_count] +"/"

	number_path = main_folder + "/" + every_iter[0] +"/"

	symbol_path =Image.open( main_folder + "/" + every_iter[1] +"/" +sub_folder[current_folder_count]+".png")

	size_number =(70,70)

	size_symbol =(90,100)

	size_main =(450,666)

	symbol_path_resize = symbol_path.resize(size_symbol)

	for image_file in os.listdir(full_path):

		default_card = Image.open("H:/Cards Anime/card.png")

		x = default_card.copy()

		clean_name_main = os.path.basename(image_file).split(".")[0]

		printed_num = Image.open(f'{number_path}{clean_name_main}'+".png") 	

		printed_num_resize = printed_num.resize(size_number)

		printed_img = Image.open(f'{full_path}{image_file}')

		pic_print = printed_img.resize(size_main)

		upper_num =(40,60,110,130)

		lower_num = (620,800,690,870)

		upper_sym = (40,140,130,240)

		lower_sym = (620,695,710,795)

		main = (150,160,600,826)

		pic = [pic_print,symbol_path_resize,symbol_path_resize,printed_num_resize,printed_num_resize]

		box = [main,upper_sym,lower_sym,upper_num,lower_num]

		for t in range(0,5):

			u = pic[t]

			v = box[t]

			x.paste(u,v)

			x.save(f'{output_folder}{clean_name_main}{sub_folder[current_folder_count]}.png')

			x = Image.open(f'{output_folder}{clean_name_main}{sub_folder[current_folder_count]}.png')

		x.show()
		
	current_folder_count += 1

	# if current_folder_count ==4 :

	# 	temp = Image.open(f'{full_path}{image_file}')

	# 	temp.show()

	# 	break