def remove_transparency(im, bg_colour=(255, 255, 255)):

    # Only process if image has transparency
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format

        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im
def convert_to_grayscale(arr):
  # convert from np.array to PIL image, convert to grayscale and convert it back to np.array
  return np.array(remove_transparency(Image.fromarray(arr)).convert('L'))


positive_gray_images = list(map(convert_to_grayscale, positive_images))
negative_gray_images = list(map( convert_to_grayscale, negative_images))


print(f"Shapes of positives images : { set([i.shape for i in positive_gray_images])}")
print(f"Shapes of negatives images : { set([i.shape for i in negative_gray_images])}")

print(len(positive_gray_images), len(positive_labels))
print(len(negative_gray_images), len(negative_labels))

test_positive_gray_images = list(map(convert_to_grayscale, test_positive_images))
test_negative_gray_images = list(map( convert_to_grayscale, test_negative_images))

print(len(test_positive_gray_images), len(test_positive_labels))
print(len(test_negative_gray_images), len(test_negative_labels))

from PIL import Image, ImageEnhance

def increase_sharpness(image):
    # Convert ndarray to PIL Image
    pil_image = Image.fromarray(image)

    # Enhance the sharpness
    enhancer = ImageEnhance.Sharpness(pil_image)
    sharpened_image = enhancer.enhance(5.0)  # Increase the sharpness factor

    # Convert PIL Image back to ndarray
    sharpened_array = np.array(sharpened_image)

    return sharpened_array


positive_sharp = [ increase_sharpness(i) for i in positive_gray_images]
negative_sharp = [ increase_sharpness(i) for i in negative_gray_images]

positive_clahe = [ clahe(i).numpy() for i in positive_gray_images ]
negative_clahe = [ clahe(i).numpy() for i in negative_gray_images ]


all_images = np.concatenate((positive_gray_images,positive_sharp, positive_clahe, negative_gray_images, negative_sharp, negative_clahe))
all_labels = np.concatenate((positive_labels, positive_labels, positive_labels, negative_labels, negative_labels, negative_labels))


test_images = np.concatenate([test_positive_gray_images,test_negative_gray_images])
test_labels = np.concatenate([test_positive_labels,test_negative_labels])


print(len(all_images))
print(len(all_labels))

print(len(test_images))
print(len(test_labels))

