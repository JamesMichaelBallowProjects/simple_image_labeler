import os, sys
import cv2

from sil_parser import Parser
import cv2_helper as CVHelper
import files as Files


# global
PARSER = Parser(sys.argv[1:])
print(PARSER.args)
sys.exit()

outFolder = "./test-images/out"
inFolder = "./test-images/"

# check input and output folders
Files.check_input_folder_exists(folder_path=inFolder)
Files.create_output_folder(folder_path=outFolder)

# process images
for imageName in Files.grab_next_image(inFolder):

    # obtain image
    imageMat = CVHelper.get_frame(
        image_path=f"{inFolder}/{imageName}"
    )
    imageMatShow = imageMat.copy()

    # show image and label
    buffer = ""
    while True:
        # display image and await user key press
        CVHelper.show_frame(image_mat_object=imageMatShow)
        key = CVHelper.get_key_in_render()

        #options
        # --- quit labeling altogether
        if key in [ord('=')]:  # press '=' to quit
            # lastBuffer = buffer
            print(buffer)
            sys.exit()

        # --- delete last entry in label
        elif key == ord("/"):
            buffer = buffer[:-1]
            imageMatShow = imageMat.copy()
            CVHelper.print_label_to_image(
                image=imageMatShow,
                text_to_print=buffer,
                custom_text_color='#30E5CD'
            )

        # --- save label and move on to next image
        elif key == ord("`"):
            imgExtension = imageName.split(".")[1]
            success = CVHelper.label_image(
                image_object=imageMatShow,
                labeled_img_full_path=f"{outFolder}/{buffer}.{imgExtension}"
            )
            if success:
                break
            else:
                print("That label already exists, fix your current label and save again.")

        # --- skip image (don't label it)
        elif key == ord(','):
            print(f"Skipped image: [{imageName}]")
            break

        # --- keys to type out label
        elif key != 255:  # 255 is "a special character to keep key non-empty each iteration"
            buffer += chr(key)
            CVHelper.print_label_to_image(
                image=imageMatShow,
                text_to_print=buffer,
                custom_text_color='#30E5CD'
            )
    # close image window
    CVHelper.close_preview()