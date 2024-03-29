import sys

from sil_parser import Parser
import cv2_helper as CVHelper
import files as Files


# global
PARSER = Parser(sys.argv[1:])
ARGS = PARSER.args


# check input and output folders
Files.check_input_folder_exists(folder_path=ARGS.input_folder)
Files.create_output_folder(folder_path=ARGS.output_folder)

# process images
for imageName in Files.grab_next_image(ARGS.input_folder):

    # obtain image
    imageMat = CVHelper.get_frame(
        image_path=f"{ARGS.input_folder}/{imageName}"
    )
    imageMatShow = CVHelper.scale_with_aspect(
        image_mat_object=imageMat.copy()
    )

    # show image and label
    buffer = ""
    while True:
        # display image and await user key press
        CVHelper.show_frame(image_mat_object=imageMatShow)
        key = CVHelper.get_key_in_render()

        #options
        # --- quit labeling altogether
        if key in [ord('=')]:
            sys.exit()

        # --- delete last entry in label
        elif key == ord("/"):
            buffer = buffer[:-1]
            imageMatShow = imageMat.copy()
            CVHelper.print_label_to_image(
                image=imageMatShow,
                text_to_print=buffer,
                custom_text_color=ARGS.label_preview_color,
                custom_text_size=ARGS.label_preview_size
            )

        # --- save label and move on to next image
        elif key == ord("`"):
            imgExtension = imageName.split(".")[1]
            success = CVHelper.label_image(
                image_object=imageMat,
                labeled_img_full_path=f"{ARGS.output_folder}/{buffer}.{imgExtension}"
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
                custom_text_color=ARGS.label_preview_color,
                custom_text_size=ARGS.label_preview_size
            )

    # close image window
    CVHelper.close_preview()