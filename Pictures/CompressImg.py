import cv2


class Compress_img:

    def __init__(self, img_path):
        self.img_path = img_path
        self.img_name = img_path.split('/')[-1]

    def compress_img_CV(self, compress_rate=0.5, show=False):
        img = cv2.imread(self.img_path)
        heigh, width = img.shape[:2]

        img_resize = cv2.resize(img, (int(width*compress_rate), int(heigh*compress_rate)),
                                interpolation=cv2.INTER_AREA)
        cv2.imwrite(self.img_name, img_resize)
        print("Already compress %s" % (self.img_name),
              "with compress rate", compress_rate)
        if show:
            cv2.imshow(self.img_name, img_resize)
            cv2.waitKey(0)


if __name__ == '__main__':
    img_path = input("Please the Image name that you want to compress:")
    compress = Compress_img(img_path)
    compress.compress_img_CV()
