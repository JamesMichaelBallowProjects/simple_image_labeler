import os
import cv2

LABEL_SIZE_DECODER = {
    "tiny": 1,
    "small": 2,
    "medium": 3,
    "large": 4
}

def hex_to_rgb(hex_code):
    if hex_code == "":
        return ""
    hex_code = hex_code.lstrip('#')
    red = int(hex_code[0:2], 16)
    green = int(hex_code[2:4], 16)
    blue = int(hex_code[4:6], 16)

    # cv uses BGR order
    return (blue, green, red)

def scale_with_aspect(
    image_mat_object: object
) -> object:
    h, w, _ = image_mat_object.shape
    newW = max(500,w)
    newH = int(h * (newW/w))
    print(newW, int(newH))
    return cv2.resize(
        image_mat_object,
        (newW, newH)
    )

def get_frame(
    image_path:str
) -> int:
    return cv2.imread(image_path)

def show_frame(
    image_mat_object: object
) -> None:
    cv2.imshow("image-to-be-labeled", image_mat_object)

def close_preview():
    cv2.destroyAllWindows()

def get_key_in_render():
    return cv2.waitKey(1) & 0xFF

def print_label_to_image(
    image: object,
    text_to_print: str,
    custom_text_color: str = '',
    custom_text_size: str = 'small'
) -> None:

    # initialize
    # --- fixed text items
    font = cv2.FONT_HERSHEY_PLAIN
    coord = (50,50)
    thickness = 1
    lineType = cv2.LINE_AA

    # --- set size
    if custom_text_size:
        textSize = LABEL_SIZE_DECODER[custom_text_size]
    else:
        textSize = 1

    # --- set color
    if custom_text_color and custom_text_color[0] == "#":
        textColor = hex_to_rgb(custom_text_color)
    else:
        textColor = (230, 34, 203)

    # print text to image
    cv2.putText(
        image,
        text_to_print,
        coord,
        font,
        textSize,
        textColor,
        thickness,
        lineType
    )

def label_image(
    image_object: object,
    labeled_img_full_path: str
) -> None:
    if os.path.isfile(labeled_img_full_path):
        return False
    else:
        cv2.imwrite(labeled_img_full_path, image_object)
        return True