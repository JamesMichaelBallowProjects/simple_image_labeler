import os
import cv2


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
    text_to_print: str
) -> None:

    # initialize
    font = cv2.FONT_HERSHEY_SIMPLEX
    coord = (50,50)
    fontScale = 1
    color = {
        'green': (27, 245, 0),
        'magenta': (230, 34, 203)
    }
    thickness = 2
    lineType = cv2.LINE_AA

    # print text to image
    cv2.putText(
        image,
        text_to_print,
        coord,
        font,
        fontScale,
        color['magenta'],
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