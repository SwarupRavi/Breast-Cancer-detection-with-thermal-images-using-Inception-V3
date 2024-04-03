training_positive = 'images/training/positive'
training_negative = 'images/training/negative'
positive_images = []
negative_images = []
positive_labels = []
negative_labels = []

for folder in os.listdir(training_positive):
  path = os.path.join(training_positive, folder , 'Segmentadas')
  for filename in os.listdir(path):
    if filename.endswith('.png'):
      img = Image.open(os.path.join(path, filename))
      positive_images.append(np.array(img))
positive_labels = np.ones(len(positive_images))  # Set positive labels as 1

for folder in os.listdir(training_negative):
  path = os.path.join(training_negative, folder , 'Segmentadas')
  for filename in os.listdir(path):
    if filename.endswith('.png'):
      img = Image.open(os.path.join(path, filename))
      negative_images.append(np.array(img))
negative_labels = np.zeros(len(negative_images))  # Set positive labels as 0

print(f" Number of healthy scans: {len(negative_images)} \n Number of scans with breast cancer: {len(positive_images)} " )

testing_positive = 'images/testing/positive'
testing_negative = 'images/testing/negative'
test_positive_images = []
test_negative_images = []
test_positive_labels = []
test_negative_labels = []
for folder in os.listdir(testing_positive):
  path = os.path.join(testing_positive, folder , 'Segmentadas')
  for filename in os.listdir(path):
    if filename.endswith('.png'):
      img = Image.open(os.path.join(path, filename))
      test_positive_images.append(np.array(img))
test_positive_labels = np.ones(len(test_positive_images))  # Set positive labels as 1
for folder in os.listdir(testing_negative):
  path = os.path.join(testing_negative, folder , 'Segmentadas')
  for filename in os.listdir(path):
    if filename.endswith('.png'):
      img = Image.open(os.path.join(path, filename))
      test_negative_images.append(np.array(img))
test_negative_labels = np.zeros(len(test_negative_images))  # Set positive labels as 0

print(f" Number of healthy scans: {len(test_negative_images)} \n Number of scans with breast cancer: {len(test_positive_images)} " )

