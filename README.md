<img src="" alt="image here of labeler" width=200>


# Simple Image Labeler (SIL)
SIL is a very simple tool that is made to iterate over images quickly to assign a label to them. For now, assigning a label means renaming the image with a string that signifies what kind of image it is.

SIL was created because I needed to have a means of manually labeling images that would expedite the labeling process, minimize labeling errors, and to eliminate the administrative steps of clicking on each image to label it. I used a program very similar to this one for my master's thesis, but I have since attempted to make it better for others to use.


<img src="" alt="gif here of labeler" width=200>

# How to Use
## Execution
This is a `python` package and it was developed for use on a machine running `WINDOWS`. There is a single entry point, and it's called `image_label.py`. The other files in the package are helper functions to allow others to take snippets of logic to use in their own tools.

To start this tool, you simply use:

```python
python image_label.py <args>
```

Here is what will happen:

1. A window will pop up containing the first image inside of `--input-folder`.
2. You will provide the label you want for the first image and hit a special key to save the label.
3. You will be shown the next image from inside `--input-folder` and steps (1) and (2) will repeat until either you elect to stop the labeling process or you run out of images to label.

## Input Parameters
#### Required
```
--input-folder
--output-folder
```
#### Optional
```
--label-preview-color
--label-preview-size
```

## Use
1. Initiate the program.
2. A window will pop up containing the first image inside of `--input-folder`.
    > __NOTE__: Look at your machine's task bar to see if the window is open, but not active on your screen. It may contain the python logo as the task item on your task bar.
3. Make the window active by either clicking on it (don't click on your command line).
4. Look at the image being shown in the window, and use your keyboard to type a label for the image. As you type the label, it will be previewed on TOP of the image in a discernable color.
    >__NOTE__: this is just a preview, and the text will not be printed on *top* of your image, it's just to help you see what you are trying to label it.
5. Using the special character to save the image, you can save the image and move on immediately to the next image.
6. You can skip an image and you can also quit labeling immediately by pressing special keys for each of these actions.

That's it! It's that __*simple*__!

## Allowable and Special Keys

Allowable Keys for a label
```ascii
Alphabet - [A-Za-z]
Symbols - [~!@#$%^&*()_+]
```

Special Keys for Execution
```
Remove Last Character (Delete) --> [/]
Accept Label for Image (Save)  --> [`] (same btn as ~)
Immediately Stop (Quit)        --> [=]
```