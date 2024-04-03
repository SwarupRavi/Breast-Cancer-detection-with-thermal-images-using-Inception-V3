xtrain, xtest, ytrain, ytest = train_test_split(all_images, all_labels, test_size=0.2, random_state=42)

print(f'xtrain shape: {xtrain.shape} \n ytrain shape: {ytrain.shape}')

print(f'xtest shape: {test_images.shape} \n ytest shape: {test_labels.shape}')

print(f'xtest shape: {xtest.shape} \n ytest shape: {ytest.shape}')

img_h = 480
img_w = 640
classes = 1 # positive/negative class
epochs = 3
batch_size = 32

inception = InceptionV3(input_shape=(480, 640, 3), weights='imagenet', include_top = False)

unfreeze_from_layer = -2

# Freeze all layers
for layer in inception.layers:
    layer.trainable = False
# Unfreeze the layers from the specified index onwards
for layer in inception.layers[unfreeze_from_layer:]:
    layer.trainable = True

input_tensor = Input(shape=(img_h,img_w,1))
x = Conv2D(3,(3,3),padding='same')(input_tensor)    # x has a dimension of (img_height,img_width,3)
x = inception(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
out = Dense(classes, activation = 'sigmoid')(x)

model = Model(inputs = input_tensor, outputs = out)
model.summary()

model.compile(loss= 'binary_crossentropy', optimizer=SGD(learning_rate=0.0001), metrics=['acc'] )

history = model.fit(x= xtrain, y = ytrain, batch_size=batch_size, epochs = epochs)

loss, accuracy = model.evaluate(xtest, ytest)

print('Test Loss:', loss)
print('Test Accuracy:', accuracy)

pred_vals = model.predict(xtest)
predicted = (pred_vals > 0.5 ).astype('int32')
actual = ytest

confusion_matrix( actual, predicted)


confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [True, False])

cm_display.plot()
plt.show()

predicted = ( model.predict(test_images) > 0.6).astype('int32')
actual = test_labels

confusion_matrix( actual, predicted)


loss, accuracy = model.evaluate(test_images, test_labels)

print('Test Loss:', loss)
print('Test Accuracy:', accuracy)


confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [True, False])

cm_display.plot()
plt.show()




