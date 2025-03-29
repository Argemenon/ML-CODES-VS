# Following are the definitions which will be used in Tensorflow Project
import numpy as np
from matplotlib import pyplot as plt



def view_classify(image, probabilities): #function to display predictions by the neural network
    fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
    ax1.imshow(image, cmap='gray')
    ax1.axis('off')
    ax2.barh(np.arange(10), probabilities)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    ax2.set_title('Class Probability')
    ax2.set_xlim(0,1.1)
    plt.tight_layout()
    plt.show()

def plot_learning_curve (history_model, acc= None ,name = 'learning curve'):
    plt.plot(
        range(1, int(len(history_model.history['accuracy'])+1)),
        history_model.history['accuracy'],
        label = 'accuracy while learning'
        )
    plt.title(name)
    if acc is not None:
        plt.axhline(acc, color = 'green', linestyle = '--', label = f'accuracy on test images ({acc*100:.2f}%)')
    plt.xlabel('No of learning cycles')
    plt.legend(loc = 'lower right')
    plt.ylabel('Accuracy')
    plt.ylim(top = 1)
    plt.show()

def test_acc(model, test_images, test_labels):
    test_loss, test_accuracy = model.evaluate(test_images, test_labels)
    print(f'Accuracy of the neural network on the {test_images.shape[0]} test images: {test_accuracy * 100:.2f}%')
    return test_accuracy








