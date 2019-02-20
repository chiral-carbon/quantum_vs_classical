from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

def convert(imgf, labelf, outf, n):
    filename = open(outf, "w")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        filename.write(",".join(str(pix) for pix in image)+"\n")
    
    filename.close()

convert(train_images, train_labels, "mnist_train.csv", 60000)
convert(test_images, test_labels, "mnist_test.csv", 10000)